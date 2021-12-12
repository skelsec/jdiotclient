import ssl
import asyncio
import traceback
from typing import List, Dict, Awaitable, cast

from jdiotclient import logger
from jdiotclient._version import __version__
from jdiotclient.pheripheral import JDIoTPheripheralBase
from jdiotclient.protocol.python.jdiotprotocol_pb2 import *
import websockets
from websockets.client import WebSocketClientProtocol


class JDIoTClient:
	def __init__(self, url:str, maintype:str, peripherals:List[JDIoTPheripheralBase] = [], description:str = '', ssl_ctx:ssl.SSLContext = None, subtype:str = '', username:str = '', password:str = ''):
		self.url = url
		self.username = username
		self.password = password
		self.ssl_ctx = ssl_ctx
		self.maintype = maintype
		self.subtype = subtype
		self.version = __version__
		self.description = description
		self.peripherals = peripherals
		self.__registrationToken = None
		self.diconnected_evt:asyncio.Event = None
		self.disconnect_cb:Awaitable[None] = None
		self.connected_evt:asyncio.Event = None
		self.registered_evt:asyncio.Event = None
		self.__pheripherals_out_q:asyncio.Queue = None
		self.__ws = None
		self.__current_peritherals:Dict[str, JDIoTPheripheralBase] = {} #token -> Pheripheral
		self.__current_pheripheral_token = 1
		self.__is_registered:bool = False
		self.__main_task:asyncio.Task = None

	def __get_pheripheral_token(self):
		t = self.__current_pheripheral_token
		self.__current_pheripheral_token += 1
		return str(t)
	
	def get_registration_req(self):
		res = HardwareRegisterRequest()
		res.mainModelType = self.maintype
		res.subModelType = self.subtype
		res.version = self.version
		res.description = self.description
		if self.username is not None:
			res.username = self.username
		if self.password is not None:
			res.password = self.password
		return res

	async def __register(self, websocket:WebSocketClientProtocol):
		try:
			logger.info('[+] Registering with server...')
			# registers the hardware to the server
			msg = self.get_registration_req()
			packet = Packet()
			packet.token = '0'
			packet.cmd = CommandType.HWREGISTERREQ
			packet.data = msg.SerializeToString()
			await websocket.send(packet.SerializeToString())
			while websocket.open is True:
				data_raw = await websocket.recv()
				packet = Packet()
				packet.ParseFromString(data_raw)
				if packet.cmd == CommandType.OK:
					break
				elif packet.cmd == CommandType.ERR:
					errpacket = ErrorMsg()
					errpacket.ParseFromString(packet.data)
					raise Exception('Registration failed! Reason: %s' % errpacket.message)
				elif packet.cmd == CommandType.HWREGISTERRESP:
					regres = HardwareRegisterResponse()
					regres.ParseFromString(packet.data)
					self.__registrationToken = regres.registrationToken
			
			logger.info('[+] Registration sucsessful! Our device token is: %s' % self.__registrationToken)
			x = asyncio.create_task(self.__monitor_pheripherals(websocket))
			self.__ws = websocket
			self.__is_registered = True

			for pheripheral in self.peripherals:
				_, err = await self.add_pheripheral(pheripheral)
				if err is not None:
					raise err
			self.registered_evt.set()
			return True, None
		except Exception as e:
			logger.error('[-] Registration failed!')
			traceback.print_exc()
			return None, e
	
	async def add_pheripheral(self, pheripheral: JDIoTPheripheralBase):
		try:
			logger.info('[+] Adding pheripheral...')
			if self.__is_registered is False:
				raise Exception("Device is not yet registered!")
			pin_q = asyncio.Queue()
			pheripheral.registrationToken = self.__get_pheripheral_token()
			pheripheral.set_in_q(pin_q)
			pheripheral.set_out_q(self.__pheripherals_out_q)
			pheripheral.client_disconnected_evt = self.diconnected_evt
			self.__current_peritherals[pheripheral.registrationToken] = pheripheral
			asyncio.create_task(pheripheral.run())
			descriptor = pheripheral.get_descriptor()
			pamsg = PeripheralAdded()
			pamsg.peripheral.CopyFrom(descriptor)
			packet = Packet()
			packet.token = self.__registrationToken
			packet.cmd = CommandType.PERIPHERALADDED
			packet.data = pamsg.SerializeToString()
			await self.__ws.send(packet.SerializeToString())
		
			return True, None
		except Exception as e:
			logger.error('[-] Failed to add peripheral!')
			traceback.print_exc()
			return None, e
	
	async def __monitor_pheripherals(self, websocket:WebSocketClientProtocol):
		try:
			while not self.diconnected_evt.is_set() and websocket.open is True:
				msg = await self.__pheripherals_out_q.get()
				msg = cast(PeripheralMessage, msg)
				packet = Packet()
				packet.cmd = CommandType.PERIPHERALMESSAGE
				packet.token = self.__registrationToken
				packet.data = msg.SerializeToString()
				await websocket.send(packet.SerializeToString())

		except Exception as e:
			logger.error('[-] Peripheral monitoring failed!')
			traceback.print_exc()
	
	async def __monitor_incoming(self):
		try:
			while not self.diconnected_evt.is_set() and self.__ws.open is True:
				data_raw = await self.__ws.recv()
				logger.debug('Incoming data: %s' % data_raw)
				packet = Packet()
				packet.ParseFromString(data_raw)
				try:
					if packet.cmd == CommandType.OK:
						logger.info('[-] Server removed our device.')
						break
					elif packet.cmd == CommandType.ERR:
						errpacket = ErrorMsg()
						errpacket.ParseFromString(packet.data)
						raise Exception('Registration failed! Reason: %s' % errpacket.message)
					elif packet.cmd == CommandType.PERIPHERALMESSAGE:
						msg = PeripheralMessage()
						if msg.peripheralToken in self.__current_peritherals:
							await self.__current_peritherals[msg.pheripheralToken].__in_q.put(msg)
				except Exception as e:
					traceback.print_exc()
		except Exception as e:
			traceback.print_exc()
		finally:
			await self.disconnect()
	
	async def disconnect(self):
		self.__main_task.cancel()

	
	async def __main(self):
		try:
			async with websockets.connect(self.url) as websocket:
				logger.info('[+] Connected to server!')
				self.connected_evt.set()
				_, err = await self.__register(websocket)
				if err is not None:
					raise err

				await self.__monitor_incoming()
			
			self.diconnected_evt.set()
			if self.disconnect_cb is not None:
				await self.disconnect_cb()
		except Exception as e:
			traceback.print_exc()
		finally:
			await self.disconnect()

	async def run(self):
		try:
			self.diconnected_evt = asyncio.Event()
			self.connected_evt = asyncio.Event()
			self.registered_evt = asyncio.Event()
			self.__pheripherals_out_q = asyncio.Queue()
			self.__main_task = asyncio.create_task(self.__main())
			return True, None
		except Exception as e:
			return None, e




