import asyncio
import traceback
import logging

from jdiotclient import logger
from jdiotclient.client import JDIoTClient
from jdiotclient.pheripheral import JDIoTCameraPeripheral
from jdiotclient.protocol.python.jdiotprotocol_pb2 import *

import cv2
import threading
import time

class CVCameraPeripheral(JDIoTCameraPeripheral):
	def __init__(self, camera_id, vtype:VideoType, width:int, height:int, bpp:int, fps_max:int = 10, description:str = "", maintype:str = "SIMPLE-CAM", subtype:str = ""):
		JDIoTCameraPeripheral.__init__(self, vtype, width, height, bpp, description = description, maintype = maintype, subtype = subtype)
		self.camera_id = camera_id
		self.fps_max = fps_max
		self._cam = None
		self.loop = None

	def videoloop(self):
		while True:
			ret, frame = self._cam.read()
			if ret is True:
				pv = PeripheralVideo()
				pv.x = 0
				pv.y = 0
				pv.width = self.width
				pv.height = self.height
				pv.vtype = VideoType.VID_PNG
				pv.data = cv2.imencode('.png', frame)[1].tobytes()
				
				asyncio.run_coroutine_threadsafe(self.send_video(pv), self.loop)
			time.sleep((1/self.fps_max))
	
	async def setup(self):
		try:
			self.loop = asyncio.get_event_loop()
			self._cam = cv2.VideoCapture(self.camera_id)
			self._cam.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
			self._cam.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
			th = threading.Thread(target=self.videoloop)
			th.start()
			return True, None
		except Exception as e:
			return False, e

	async def do_refresh(self, value):
		await self.send_bool(self.lastvalue)

async def amain():
	try:
		import argparse
		parser = argparse.ArgumentParser(description='JD IoT client for Raspberry PI GPIO')
		parser.add_argument('-v', '--verbose', action='count', default=0)
		parser.add_argument('-p', '--password', help='Password')
		parser.add_argument('-u', '--username', help='Username')
		parser.add_argument('-r', '--resolution', default='640x480', help='Width')
		parser.add_argument('--bpp', default=16, help='BPP')
		parser.add_argument('-f', '--fps', default=10, help='FPS limiter')
		parser.add_argument('-d', '--description', default="Camera", help='description')
		parser.add_argument('url', help='Websockets URL of the JDIOT server. Should start with "ws://" or "wss://" (latter is for SSL/TLS)')
		parser.add_argument('camid', type=int, help='Camera ID')
		args = parser.parse_args()

		if args.verbose == 1:
			logger.setLevel(logging.INFO)
		
		if args.verbose == 1:
			logger.setLevel(logging.DEBUG)

		if args.verbose > 2:
			logger.setLevel(1) #enabling deep debug
			asyncio.get_event_loop().set_debug(True)
			logging.basicConfig(level=logging.DEBUG)
		
		if args.url.lower().startswith('ws') is False:
			raise Exception('Incorrect URL! %s' % args.url)
		
		a,b = args.resolution.lower().split('x')
		width = int(a)
		height = int(b)
		 
		
		peripherals = []
		peripherals.append(CVCameraPeripheral(args.camid, VideoType.VID_PNG, width, height, args.bpp, args.fps, args.description))
		
		client = JDIoTClient(args.url, "Virtual", peripherals, description = 'Virtual camera', subtype = '', username = args.username, password = args.password)
		_, err = await client.run()
		if err is not None:
			raise err
		await client.diconnected_evt.wait()

	except Exception as e:
		print('Failed to start! Reason: %s' % e)
		traceback.print_exc()

def main():
	asyncio.run(amain())

if __name__ == '__main__':
	main()