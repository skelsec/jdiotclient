import ssl
import inspect
import asyncio
import traceback
from typing import List, Dict, Awaitable, cast

from jdiotclient import logger
from jdiotclient.protocol.python.jdiotprotocol_pb2 import *

class JDIoTPheripheralBase:
	def __init__(self, ptype: PeripheralType, description:str = "", maintype:str = "", subtype:str = ""):
		self.maintype = maintype
		self.subtype = subtype
		self.ATTR_START = 'do_' #denotes the start of function names that can be called remotely
		self.ptype = ptype
		self.description = description
		self.registrationToken:str = None
		self.client_disconnected_evt:asyncio.Event = None
		self._in_q: asyncio.Queue = None
		self._out_q: asyncio.Queue = None
	
	def _get_command(self, command):
		return getattr(self, self.ATTR_START + command)
	
	def _get_command_args(self, command):
		args = [param for param in inspect.signature(self._get_command(command)).parameters.values()
				if param.default == param.empty]
		kwargs = [param for param in inspect.signature(self._get_command(command)).parameters.values()
				  if param.default != param.empty]
		return args, kwargs
	
	async def _run_single_command(self, command, args):
		try:
			command_real_args, command_real_kwargs = self._get_command_args(command)
		except Exception as e:
			await self.print("Unknown command '%s'" % command )
			return
		if len(args) < len(command_real_args) or len(args) > (len(command_real_args)
															  + len(command_real_kwargs)):
			await self.print("Bad command args. Usage: %s" % self._get_command_usage(command, command_real_args,
																		  command_real_kwargs))
			return

		try:
			com_func = self._get_command(command)
			if asyncio.iscoroutinefunction(com_func):
				await com_func(*args)
			else:
				com_func(*args)
			return
		except (asyncio.CancelledError):
			raise
		except Exception as ex:
			await self.print("Command %s failed: %s Exc: %s" % (command, traceback.format_tb(ex.__traceback__), ex))
	
	def command_list(self):
		return [attr[len(self.ATTR_START):]
				for attr in dir(self) if attr.startswith(self.ATTR_START)]

	
	def set_in_q(self, in_q: asyncio.Queue):
		"""Called by the JDIoTClient, don't use it manually"""
		self.__in_q = in_q
	
	def set_out_q(self, out_q: asyncio.Queue):
		"""Called by the JDIoTClient, don't use it manually"""
		self._out_q = out_q
	
	def get_descriptor(self) -> Peripheral :
		"""Override this function"""
		raise NotImplementedError()
	
	async def setup(self):
		"""Override me pls"""
		pass
	
	async def run(self):
		try:
			if hasattr(self, 'setup'):
				if asyncio.iscoroutinefunction(self.setup):
					_, err = await self.setup()
				else:
					_, err = self.setup()
				if err is not None:
					logger.info('[-] Peripheral setup returned error! Stopping peripheral!')
					raise err
				
			while not self.client_disconnected_evt.is_set():
				msg = await self.__in_q.get()
				try:
					msg = cast(PeripheralMessage, msg)
					if msg.type == PeripheralCommandType.PSTATE:
						vmsg = PeripheralState()
						vmsg.ParseFromString(msg.data)
						if vmsg.stateType == PStateType.PSTATE_BOOL:
							data = PeripheralStateBool()
							data.ParseFromString(vmsg.state)
							await self._run_single_command('bool', (data.value, msg.customtoken))

						elif vmsg.stateType == PStateType.PSTATE_INT:
							data = PeripheralStateInt()
							data.ParseFromString(vmsg.state)
							await self._run_single_command('int', (data.value, msg.customtoken))

						elif vmsg.stateType == PStateType.PSTATE_STRING:
							data = PeripheralStateString()
							data.ParseFromString(vmsg.state)
							await self._run_single_command('string', (data.value, msg.customtoken))
						
						elif vmsg.stateType == PStateType.PSTATE_BYTES:
							data = PeripheralStateBytes()
							data.ParseFromString(vmsg.state)
							await self._run_single_command('bytes', (data.value, msg.customtoken))
						
						elif vmsg.stateType == PStateType.PSTATE_TAGGED:
							data = PeripheralStateTagged()
							data.ParseFromString(vmsg.state)
							await self._run_single_command('tagged', (data.tag, data.value, msg.customtoken))

					elif msg.type == PeripheralCommandType.PAUDIO:
						raise NotImplementedError()
					elif msg.type == PeripheralCommandType.PVIDEO:
						raise NotImplementedError()
					elif msg.type == PeripheralCommandType.PREFRESH:
						await self._run_single_command('refresh', (msg.customtoken))
					else:
						raise NotImplementedError()
				except Exception as e:
					traceback.print_exc()
		except Exception as e:
			traceback.print_exc()

class JDIoTStatefulPheripheral(JDIoTPheripheralBase):
	def __init__(self, ptype:PeripheralType, cmdtype:PStateType, minValue:int = None, maxValue:int = None, stepsValue = None, description:str = "", maintype:str = "", subtype:str = ""):
		JDIoTPheripheralBase.__init__(self, ptype, description = description, maintype = maintype, subtype = subtype)
		self.cmdtype = cmdtype
		self.minValue = minValue
		self.maxValue = maxValue
		self.stepsValue = stepsValue
	
	async def send_bool(self, value:bool, customtoken:str = None):
		try:
			pval = PeripheralStateBool()
			pval.value = value
			msg = PeripheralState()
			msg.stateType = PStateType.PSTATE_BOOL
			msg.state = pval.SerializeToString()
			await self.send_state(msg, customtoken)
		except Exception as e:
			traceback.print_exc()
	
	async def send_int(self, value:int, customtoken:str = None):
		try:
			pval = PeripheralStateInt()
			pval.value = value
			msg = PeripheralState()
			msg.stateType = PStateType.PSTATE_INT
			msg.state = pval.SerializeToString()
			await self.send_state(msg, customtoken)
		except Exception as e:
			traceback.print_exc()
	
	async def send_string(self, value:str, customtoken:str = None):
		try:
			pval = PeripheralStateString()
			pval.value = value
			msg = PeripheralState()
			msg.stateType = PStateType.PSTATE_STRING
			msg.state = pval.SerializeToString()
			await self.send_state(msg, customtoken)
		except Exception as e:
			traceback.print_exc()
	
	async def send_bytes(self, value:bytes, customtoken:str = None):
		try:
			pval = PeripheralStateBytes()
			pval.value = value
			msg = PeripheralState()
			msg.stateType = PStateType.PSTATE_BYTES
			msg.state = pval.SerializeToString()
			await self.send_state(msg, customtoken)
		except Exception as e:
			traceback.print_exc()

	async def send_state(self, msg:PeripheralState, customtoken:str = None):
		try:
			res = PeripheralMessage()
			res.peripheralToken = self.registrationToken
			res.type = PeripheralCommandType.PSTATE
			res.data = msg.SerializeToString()
			if customtoken is not None:
				res.customtoken = customtoken
			await self._out_q.put(res)
		except Exception as e:
			traceback.print_exc()
	
	def get_descriptor(self) -> Peripheral :
		res = Peripheral()
		res.type = self.ptype
		res.interactive = len(self.command_list()) > 0
		res.peripheralToken = self.registrationToken
		res.description = self.description
		descriptor = PeriPheralDescriptorStateful()
		descriptor.commandtype = self.cmdtype
		descriptor.stateMinVal = 0
		descriptor.stateMaxVal = 0
		descriptor.steps = 0
		
		
		if self.minValue is not None:
			descriptor.stateMinVal = self.minValue
		if self.maxValue is not None:
			descriptor.stateMaxVal = self.maxValue
		if self.stepsValue is not None:
			descriptor.steps = self.stepsValue
		
		dwrapper = PeripheralDescriptor()
		dwrapper.mainModelType = self.maintype
		dwrapper.subModelType = self.subtype
		dwrapper.type = PeripheralDescriptorType.PD_STETFUL
		dwrapper.data = descriptor.SerializeToString()
		
		res.descriptor.CopyFrom(dwrapper)
		return res


class JDIoTCameraPheripheral(JDIoTPheripheralBase):
	def __init__(self, vtype:VideoType, width:int, height:int, bpp:int, description:str = "", maintype:str = "", subtype:str = ""):
		JDIoTPheripheralBase.__init__(self, PeripheralType.CAMERA, description = description, maintype = maintype, subtype = subtype)
		self.vtype = vtype
		self.width = width
		self.height = height
		self.bpp = bpp

	async def send_video(self, msg:PeripheralVideo, customtoken:str = None):
		try:
			res = PeripheralMessage()
			res.peripheralToken = self.registrationToken
			res.type = PeripheralCommandType.PVIDEO
			res.data = msg.SerializeToString()
			if customtoken is not None:
				res.customtoken = customtoken
			await self._out_q.put(res)
		except Exception as e:
			traceback.print_exc()
	
	def get_descriptor(self) -> Peripheral :
		res = Peripheral()
		res.mainModelType = self.mainModelType
		res.subModelType = self.subModelType
		res.type = self.ptype
		res.interactive = len(self.command_list()) > 0
		res.peripheralToken = self.registrationToken
		res.description = self.description
		descriptor = PeriPheralDescriptorVideo()
		descriptor.width = self.width
		descriptor.height = self.height
		descriptor.bpp = self.bpp
		descriptor.vtype = self.vtype
		
		dwrapper = PeripheralDescriptor()
		dwrapper.mainModelType = self.maintype
		dwrapper.subModelType = self.subtype
		dwrapper.type = PeripheralDescriptorType.PD_VIDEO
		dwrapper.data = descriptor.SerializeToString()
		res.descriptor.CopyFrom(dwrapper)
		return res
