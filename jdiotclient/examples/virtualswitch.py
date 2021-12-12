import asyncio
import traceback
import logging

from jdiotclient import logger
from jdiotclient.client import JDIoTClient
from jdiotclient.pheripheral import JDIoTStatefulPheripheral
from jdiotclient.protocol.python.jdiotprotocol_pb2 import *

class VirtualOutputPeripheral(JDIoTStatefulPheripheral):
	def __init__(self, description = "", maintype = "SIMPLE-SWITCH"):
		JDIoTStatefulPheripheral.__init__(self, PeripheralType.SWITCH, PStateType.PSTATE_BOOL, description = description, maintype = maintype)
		self.lastvalue = False

	async def setup(self):
		try:
			
			return True, None
		except Exception as e:
			return False, e
	
	async def do_bool(self, value, customtoken = None):
		self.lastvalue = value
	
	async def do_refresh(self, value):
		await self.send_bool(self.lastvalue)

class VirtualInputPeripheral(JDIoTStatefulPheripheral):
	def __init__(self, description = "", maintype = "SIMPLE-BULB"):
		JDIoTStatefulPheripheral.__init__(self, PeripheralType.PIN, PStateType.PSTATE_BOOL, description = description, maintype = maintype)
		self.lastvalue = False
		self.switch_time = 3
	
	async def __switching(self):
		while True:
			self.lastvalue = not self.lastvalue
			await self.send_bool(self.lastvalue)
			await asyncio.sleep(self.switch_time)

	async def setup(self):
		try:
			asyncio.create_task(self.__switching())
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
		parser.add_argument('url', help='Websockets URL of the JDIOT server. Should start with "ws://" or "wss://" (latter is for SSL/TLS)')
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
		
		peripherals = []
		peripherals.append(VirtualOutputPeripheral("hello?"))
		peripherals.append(VirtualInputPeripheral("h2"))
		
		client = JDIoTClient(args.url, "Virtual", peripherals, description = 'Virtual sample client', subtype = '', username = args.username, password = args.password)
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