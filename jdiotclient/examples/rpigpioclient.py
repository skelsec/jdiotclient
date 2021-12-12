import asyncio
import traceback
import logging

from jdiotclient import logger
from jdiotclient.client import JDIoTClient
from jdiotclient.pheripheral import JDIoTStatefulPheripheral
from jdiotclient.protocol.python.jdiotprotocol_pb2 import *

import RPi.GPIO as GPIO

#GPIO.BCM
#= GPIO.BOARD
class RPIGPIOOutputPeripheral(JDIoTStatefulPheripheral):
	def __init__(self, gpioport, gpiopinlayout, pull_up_down, description = "", maintype = "SIMPLE-SWITCH"):
		JDIoTStatefulPheripheral.__init__(self, PeripheralType.SWITCH, PStateType.PSTATE_BOOL, description = description, maintype = maintype)
		self.gpiopinlayout = gpiopinlayout
		self.gpioport = gpioport
		self.lastvalue = False
		self.pull_up_down = pull_up_down

	async def setup(self):
		try:
			GPIO.setmode(self.gpiopinlayout)
			GPIO.setup(self.gpioport, GPIO.OUT, pull_up_down = self.pull_up_down)

			return True, None
		except Exception as e:
			return False, e
	
	async def do_bool(self, value, customtoken = None):
		GPIO.output(self.gpioport, value)
		self.lastvalue = value
	
	async def do_refresh(self, value):
		await self.send_bool(self.lastvalue)

class RPIGPIOInputPeripheral(JDIoTStatefulPheripheral):
	def __init__(self, gpioport, gpiopinlayout, pull_up_down, description = "", maintype = "SIMPLE-BULB"):
		JDIoTStatefulPheripheral.__init__(self, PeripheralType.PIN, PStateType.PSTATE_BOOL, description = description, maintype = maintype)
		self.gpiopinlayout = gpiopinlayout
		self.gpioport = gpioport
		self.bouncetime = 500
		self.pull_up_down = pull_up_down
		self.loop = None
	
	def pin_rising(self, pin):
		asyncio.run_coroutine_threadsafe(self.send_bool(True), self.loop)

	async def setup(self):
		try:
			self.loop = asyncio.get_event_loop()
			GPIO.setmode(self.gpiopinlayout)
			GPIO.setup(self.gpioport, GPIO.IN, pull_up_down = self.pull_up_down)
			GPIO.add_event_detect(self.gpioport, GPIO.RISING, callback=self.pin_rising, bouncetime=self.bouncetime)

			return True, None
		except Exception as e:
			return False, e

async def amain():
	try:
		import argparse
		parser = argparse.ArgumentParser(description='JD IoT client for Raspberry PI GPIO')
		parser.add_argument('-v', '--verbose', action='count', default=0)
		parser.add_argument('-p', '--password', help='Password')
		parser.add_argument('-u', '--username', help='Username')
		parser.add_argument('url', help='Websockets URL of the JDIOT server. Should start with "ws://" or "wss://" (latter is for SSL/TLS)')
		parser.add_argument('peripherals', nargs='*', help = 'Peripherals')
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
		
		if len(args.peripherals) < 1:
			raise Exception('No peripheral definition set!')
		
		peripherals = []
		for peri in args.peripherals:
			pt, layout, pin, pud, description = [p.upper() for p in peri.split(':')]
			print(pt, layout, pin, pud, description)
			print(repr(description))
			if layout == 'BCM':
				boardtype = GPIO.BCM
			elif layout == 'BOARD':
				boardtype = GPIO.BOARD
			else:
				raise Exception('Pin layout must be either BCM or BOARD')
			
			pin = int(pin)

			if pud == 'PUD_UP':
				pull_up_down = GPIO.PUD_UP
			elif pud == 'PUD_OFF':
				pull_up_down = GPIO.PUD_OFF
			elif pud == 'PUD_DOWN':
				pull_up_down = GPIO.PUD_DOWN
			else:
				raise Exception('Pud must be on of the following: PUD_UP, PUD_OFF, PUD_DOWN')
			
			if pt == 'IN':
				peripherals.append(RPIGPIOInputPeripheral(pin, boardtype, description = description))
			elif pt == 'OUT':
				peripherals.append(RPIGPIOOutputPeripheral(pin, boardtype, description = description))
			else:
				raise Exception('PT must be either IN or OUT')
		
		client = JDIoTClient(args.url, "RPI", peripherals, description = 'RPI sample client', subtype = '', username = args.username, password = args.password)
		_, err = await client.run()
		if err is not None:
			raise err

	except Exception as e:
		print('Failed to start! Reason: %s' % e)
		traceback.print_exc()

def main():
	asyncio.run(amain())

if __name__ == '__main__':
	main()