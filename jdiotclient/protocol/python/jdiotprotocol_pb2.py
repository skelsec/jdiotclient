# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: jdiotprotocol.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13jdiotprotocol.proto\"\x1a\n\x08\x45rrorMsg\x12\x0e\n\x06reason\x18\x01 \x01(\t\"(\n\x06LogMsg\x12\r\n\x05level\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"N\n\x06Packet\x12\x19\n\x03\x63md\x18\x01 \x01(\x0e\x32\x0c.CommandType\x12\r\n\x05token\x18\x02 \x01(\t\x12\x11\n\x04\x64\x61ta\x18\x03 \x01(\x0cH\x00\x88\x01\x01\x42\x07\n\x05_data\"\x9c\x01\n\x17OperatorRegisterRequest\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x18\n\x0b\x64\x65scription\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08username\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x15\n\x08password\x18\x04 \x01(\tH\x02\x88\x01\x01\x42\x0e\n\x0c_descriptionB\x0b\n\t_usernameB\x0b\n\t_password\"\xc9\x01\n\x17HardwareRegisterRequest\x12\x15\n\rmainModelType\x18\x01 \x01(\t\x12\x14\n\x0csubModelType\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x18\n\x0b\x64\x65scription\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08username\x18\x05 \x01(\tH\x01\x88\x01\x01\x12\x15\n\x08password\x18\x06 \x01(\tH\x02\x88\x01\x01\x42\x0e\n\x0c_descriptionB\x0b\n\t_usernameB\x0b\n\t_password\"5\n\x18HardwareRegisterResponse\x12\x19\n\x11registrationToken\x18\x01 \x01(\t\"\xab\x01\n\x0cHardwareInfo\x12\x15\n\rmainModelType\x18\x01 \x01(\t\x12\x14\n\x0csubModelType\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x18\n\x0b\x64\x65scription\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x19\n\x11registrationToken\x18\x05 \x01(\t\x12\x18\n\x10peripheralTokens\x18\x06 \x03(\tB\x0e\n\x0c_description\".\n\x11HardwareSubscribe\x12\x19\n\x11registrationToken\x18\x01 \x01(\t\"0\n\x13HardwareUnSubscribe\x12\x19\n\x11registrationToken\x18\x01 \x01(\t\"2\n\x0fPeripheralAdded\x12\x1f\n\nperipheral\x18\x01 \x01(\x0b\x32\x0b.Peripheral\",\n\x11PeriPheralRemoved\x12\x17\n\x0fperipheralToken\x18\x01 \x01(\t\"\x99\x01\n\nPeripheral\x12\x1d\n\x04type\x18\x01 \x01(\x0e\x32\x0f.PeripheralType\x12\x13\n\x0binteractive\x18\x02 \x01(\x08\x12\x17\n\x0fperipheralToken\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12)\n\ndescriptor\x18\x05 \x01(\x0b\x32\x15.PeripheralDescriptor\"z\n\x14PeripheralDescriptor\x12\'\n\x04type\x18\x01 \x01(\x0e\x32\x19.PeripheralDescriptorType\x12\x15\n\rmainModelType\x18\x02 \x01(\t\x12\x14\n\x0csubModelType\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\"y\n\x1cPeriPheralDescriptorStateful\x12 \n\x0b\x63ommandtype\x18\x01 \x01(\x0e\x32\x0b.PStateType\x12\x13\n\x0bstateMinVal\x18\x02 \x01(\x03\x12\x13\n\x0bstateMaxVal\x18\x03 \x01(\x03\x12\r\n\x05steps\x18\x04 \x01(\x04\"b\n\x19PeriPheralDescriptorVideo\x12\r\n\x05width\x18\x01 \x01(\r\x12\x0e\n\x06height\x18\x02 \x01(\r\x12\x0b\n\x03\x62pp\x18\x03 \x01(\r\x12\x19\n\x05vtype\x18\x04 \x01(\x0e\x32\n.VideoType\"\x98\x01\n\x11PeripheralMessage\x12\x17\n\x0fperipheralToken\x18\x01 \x01(\t\x12\x18\n\x0b\x63ustomtoken\x18\x02 \x01(\tH\x00\x88\x01\x01\x12$\n\x04type\x18\x03 \x01(\x0e\x32\x16.PeripheralCommandType\x12\x11\n\x04\x64\x61ta\x18\x04 \x01(\x0cH\x01\x88\x01\x01\x42\x0e\n\x0c_customtokenB\x07\n\x05_data\"@\n\x0fPeripheralState\x12\x1e\n\tstateType\x18\x01 \x01(\x0e\x32\x0b.PStateType\x12\r\n\x05state\x18\x02 \x01(\x0c\"$\n\x13PeripheralStateBool\x12\r\n\x05value\x18\x01 \x01(\x08\"#\n\x12PeripheralStateInt\x12\r\n\x05value\x18\x01 \x01(\x03\"&\n\x15PeripheralStateString\x12\r\n\x05value\x18\x01 \x01(\t\"%\n\x14PeripheralStateBytes\x12\r\n\x05value\x18\x01 \x01(\x0c\"3\n\x15PeripheralStateTagged\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\" \n\x0fPeripheralAudio\x12\r\n\x05value\x18\x01 \x01(\x04\"o\n\x0fPeripheralVideo\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\r\n\x05width\x18\x03 \x01(\r\x12\x0e\n\x06height\x18\x04 \x01(\r\x12\x19\n\x05vtype\x18\x05 \x01(\x0e\x32\n.VideoType\x12\x0c\n\x04\x64\x61ta\x18\x06 \x01(\x0c*\x18\n\tVideoType\x12\x0b\n\x07VID_PNG\x10\x00*F\n\x18PeripheralDescriptorType\x12\x0e\n\nPD_STETFUL\x10\x00\x12\x0c\n\x08PD_VIDEO\x10\x01\x12\x0c\n\x08PD_AUDIO\x10\x02*a\n\x0ePeripheralType\x12\n\n\x06SWITCH\x10\x00\x12\x07\n\x03PIN\x10\x01\x12\n\n\x06\x43\x41MERA\x10\x02\x12\x0e\n\nMICROPHONE\x10\x03\x12\x07\n\x03GPS\x10\x04\x12\n\n\x06\x43USTOM\x10\x05\x12\t\n\x05LEVEL\x10\x06*\xfa\x01\n\x0b\x43ommandType\x12\x06\n\x02OK\x10\x00\x12\x07\n\x03\x45RR\x10\x01\x12\x07\n\x03LOG\x10\x02\x12\x11\n\rHWREGISTERREQ\x10\x03\x12\x12\n\x0eHWREGISTERRESP\x10\x04\x12\n\n\x06LISTHW\x10\x05\x12\n\n\x06HWINFO\x10\x06\x12\x12\n\x0ePERIPHERALINFO\x10\x07\x12\x13\n\x0fPERIPHERALADDED\x10\x08\x12\x15\n\x11PERIPHERALREMOVED\x10\t\x12\x15\n\x11PERIPHERALMESSAGE\x10\n\x12\x0f\n\x0bHWSUBSCRIBE\x10\x0b\x12\x11\n\rHWUNSUBSCRIBE\x10\x0c\x12\x17\n\x13OPERATORREGISTERREQ\x10\r*I\n\x15PeripheralCommandType\x12\n\n\x06PSTATE\x10\x00\x12\n\n\x06PAUDIO\x10\x01\x12\n\n\x06PVIDEO\x10\x02\x12\x0c\n\x08PREFRESH\x10\x03*e\n\nPStateType\x12\x0f\n\x0bPSTATE_BOOL\x10\x00\x12\x0e\n\nPSTATE_INT\x10\x01\x12\x11\n\rPSTATE_STRING\x10\x02\x12\x10\n\x0cPSTATE_BYTES\x10\x03\x12\x11\n\rPSTATE_TAGGED\x10\x04\x62\x06proto3')

_VIDEOTYPE = DESCRIPTOR.enum_types_by_name['VideoType']
VideoType = enum_type_wrapper.EnumTypeWrapper(_VIDEOTYPE)
_PERIPHERALDESCRIPTORTYPE = DESCRIPTOR.enum_types_by_name['PeripheralDescriptorType']
PeripheralDescriptorType = enum_type_wrapper.EnumTypeWrapper(_PERIPHERALDESCRIPTORTYPE)
_PERIPHERALTYPE = DESCRIPTOR.enum_types_by_name['PeripheralType']
PeripheralType = enum_type_wrapper.EnumTypeWrapper(_PERIPHERALTYPE)
_COMMANDTYPE = DESCRIPTOR.enum_types_by_name['CommandType']
CommandType = enum_type_wrapper.EnumTypeWrapper(_COMMANDTYPE)
_PERIPHERALCOMMANDTYPE = DESCRIPTOR.enum_types_by_name['PeripheralCommandType']
PeripheralCommandType = enum_type_wrapper.EnumTypeWrapper(_PERIPHERALCOMMANDTYPE)
_PSTATETYPE = DESCRIPTOR.enum_types_by_name['PStateType']
PStateType = enum_type_wrapper.EnumTypeWrapper(_PSTATETYPE)
VID_PNG = 0
PD_STETFUL = 0
PD_VIDEO = 1
PD_AUDIO = 2
SWITCH = 0
PIN = 1
CAMERA = 2
MICROPHONE = 3
GPS = 4
CUSTOM = 5
LEVEL = 6
OK = 0
ERR = 1
LOG = 2
HWREGISTERREQ = 3
HWREGISTERRESP = 4
LISTHW = 5
HWINFO = 6
PERIPHERALINFO = 7
PERIPHERALADDED = 8
PERIPHERALREMOVED = 9
PERIPHERALMESSAGE = 10
HWSUBSCRIBE = 11
HWUNSUBSCRIBE = 12
OPERATORREGISTERREQ = 13
PSTATE = 0
PAUDIO = 1
PVIDEO = 2
PREFRESH = 3
PSTATE_BOOL = 0
PSTATE_INT = 1
PSTATE_STRING = 2
PSTATE_BYTES = 3
PSTATE_TAGGED = 4


_ERRORMSG = DESCRIPTOR.message_types_by_name['ErrorMsg']
_LOGMSG = DESCRIPTOR.message_types_by_name['LogMsg']
_PACKET = DESCRIPTOR.message_types_by_name['Packet']
_OPERATORREGISTERREQUEST = DESCRIPTOR.message_types_by_name['OperatorRegisterRequest']
_HARDWAREREGISTERREQUEST = DESCRIPTOR.message_types_by_name['HardwareRegisterRequest']
_HARDWAREREGISTERRESPONSE = DESCRIPTOR.message_types_by_name['HardwareRegisterResponse']
_HARDWAREINFO = DESCRIPTOR.message_types_by_name['HardwareInfo']
_HARDWARESUBSCRIBE = DESCRIPTOR.message_types_by_name['HardwareSubscribe']
_HARDWAREUNSUBSCRIBE = DESCRIPTOR.message_types_by_name['HardwareUnSubscribe']
_PERIPHERALADDED = DESCRIPTOR.message_types_by_name['PeripheralAdded']
_PERIPHERALREMOVED = DESCRIPTOR.message_types_by_name['PeriPheralRemoved']
_PERIPHERAL = DESCRIPTOR.message_types_by_name['Peripheral']
_PERIPHERALDESCRIPTOR = DESCRIPTOR.message_types_by_name['PeripheralDescriptor']
_PERIPHERALDESCRIPTORSTATEFUL = DESCRIPTOR.message_types_by_name['PeriPheralDescriptorStateful']
_PERIPHERALDESCRIPTORVIDEO = DESCRIPTOR.message_types_by_name['PeriPheralDescriptorVideo']
_PERIPHERALMESSAGE = DESCRIPTOR.message_types_by_name['PeripheralMessage']
_PERIPHERALSTATE = DESCRIPTOR.message_types_by_name['PeripheralState']
_PERIPHERALSTATEBOOL = DESCRIPTOR.message_types_by_name['PeripheralStateBool']
_PERIPHERALSTATEINT = DESCRIPTOR.message_types_by_name['PeripheralStateInt']
_PERIPHERALSTATESTRING = DESCRIPTOR.message_types_by_name['PeripheralStateString']
_PERIPHERALSTATEBYTES = DESCRIPTOR.message_types_by_name['PeripheralStateBytes']
_PERIPHERALSTATETAGGED = DESCRIPTOR.message_types_by_name['PeripheralStateTagged']
_PERIPHERALAUDIO = DESCRIPTOR.message_types_by_name['PeripheralAudio']
_PERIPHERALVIDEO = DESCRIPTOR.message_types_by_name['PeripheralVideo']
ErrorMsg = _reflection.GeneratedProtocolMessageType('ErrorMsg', (_message.Message,), {
  'DESCRIPTOR' : _ERRORMSG,
  '__module__' : 'jdiotprotocol_pb2'
  # @@protoc_insertion_point(class_scope:ErrorMsg)
  })
_sym_db.RegisterMessage(ErrorMsg)

LogMsg = _reflection.GeneratedProtocolMessageType('LogMsg', (_message.Message,), {
  'DESCRIPTOR' : _LOGMSG,
  '__module__' : 'jdiotprotocol_pb2'
  # @@protoc_insertion_point(class_scope:LogMsg)
  })
_sym_db.RegisterMessage(LogMsg)

Packet = _reflection.GeneratedProtocolMessageType('Packet', (_message.Message,), {
  'DESCRIPTOR' : _PACKET,
  '__module__' : 'jdiotprotocol_pb2'
  # @@protoc_insertion_point(class_scope:Packet)
  })
_sym_db.RegisterMessage(Packet)

OperatorRegisterRequest = _reflection.GeneratedProtocolMessageType('OperatorRegisterRequest', (_message.Message,), {
  'DESCRIPTOR' : _OPERATORREGISTERREQUEST,
  '__module__' : 'jdiotprotocol_pb2'
  # @@protoc_insertion_point(class_scope:OperatorRegisterRequest)
  })
_sym_db.RegisterMessage(OperatorRegisterRequest)

HardwareRegisterRequest = _reflection.GeneratedProtocolMessageType('HardwareRegisterRequest', (_message.Message,), {
  'DESCRIPTOR' : _HARDWAREREGISTERREQUEST,
  '__module__' : 'jdiotprotocol_pb2'
  # @@protoc_insertion_point(class_scope:HardwareRegisterRequest)
  })
_sym_db.RegisterMessage(HardwareRegisterRequest)

HardwareRegisterResponse = _reflection.GeneratedProtocolMessageType('HardwareRegisterResponse', (_message.Message,), {
  'DESCRIPTOR' : _HARDWAREREGISTERRESPONSE,
  '__module__' : 'jdiotprotocol_pb2'
  # @@protoc_insertion_point(class_scope:HardwareRegisterResponse)
  })
_sym_db.RegisterMessage(HardwareRegisterResponse)

HardwareInfo = _reflection.GeneratedProtocolMessageType('HardwareInfo', (_message.Message,), {
  'DESCRIPTOR' : _HARDWAREINFO,
  '__module__' : 'jdiotprotocol_pb2'
  # @@protoc_insertion_point(class_scope:HardwareInfo)
  })
_sym_db.RegisterMessage(HardwareInfo)

HardwareSubscribe = _reflection.GeneratedProtocolMessageType('HardwareSubscribe', (_message.Message,), {
  'DESCRIPTOR' : _HARDWARESUBSCRIBE,
  '__module__' : 'jdiotprotocol_pb2'
  # @@protoc_insertion_point(class_scope:HardwareSubscribe)
  })
_sym_db.RegisterMessage(HardwareSubscribe)

HardwareUnSubscribe = _reflection.GeneratedProtocolMessageType('HardwareUnSubscribe', (_message.Message,), {
  'DESCRIPTOR' : _HARDWAREUNSUBSCRIBE,
  '__module__' : 'jdiotprotocol_pb2'
  # @@protoc_insertion_point(class_scope:HardwareUnSubscribe)
  })
_sym_db.RegisterMessage(HardwareUnSubscribe)

PeripheralAdded = _reflection.GeneratedProtocolMessageType('PeripheralAdded', (_message.Message,), {
  'DESCRIPTOR' : _PERIPHERALADDED,
  '__module__' : 'jdiotprotocol_pb2'
  # @@protoc_insertion_point(class_scope:PeripheralAdded)
  })
_sym_db.RegisterMessage(PeripheralAdded)

PeriPheralRemoved = _reflection.GeneratedProtocolMessageType('PeriPheralRemoved', (_message.Message,), {
  'DESCRIPTOR' : _PERIPHERALREMOVED,
  '__module__' : 'jdiotprotocol_pb2'
  # @@protoc_insertion_point(class_scope:PeriPheralRemoved)
  })
_sym_db.RegisterMessage(PeriPheralRemoved)

Peripheral = _reflection.GeneratedProtocolMessageType('Peripheral', (_message.Message,), {
  'DESCRIPTOR' : _PERIPHERAL,
  '__module__' : 'jdiotprotocol_pb2'
  # @@protoc_insertion_point(class_scope:Peripheral)
  })
_sym_db.RegisterMessage(Peripheral)

PeripheralDescriptor = _reflection.GeneratedProtocolMessageType('PeripheralDescriptor', (_message.Message,), {
  'DESCRIPTOR' : _PERIPHERALDESCRIPTOR,
  '__module__' : 'jdiotprotocol_pb2'
  # @@protoc_insertion_point(class_scope:PeripheralDescriptor)
  })
_sym_db.RegisterMessage(PeripheralDescriptor)

PeriPheralDescriptorStateful = _reflection.GeneratedProtocolMessageType('PeriPheralDescriptorStateful', (_message.Message,), {
  'DESCRIPTOR' : _PERIPHERALDESCRIPTORSTATEFUL,
  '__module__' : 'jdiotprotocol_pb2'
  # @@protoc_insertion_point(class_scope:PeriPheralDescriptorStateful)
  })
_sym_db.RegisterMessage(PeriPheralDescriptorStateful)

PeriPheralDescriptorVideo = _reflection.GeneratedProtocolMessageType('PeriPheralDescriptorVideo', (_message.Message,), {
  'DESCRIPTOR' : _PERIPHERALDESCRIPTORVIDEO,
  '__module__' : 'jdiotprotocol_pb2'
  # @@protoc_insertion_point(class_scope:PeriPheralDescriptorVideo)
  })
_sym_db.RegisterMessage(PeriPheralDescriptorVideo)

PeripheralMessage = _reflection.GeneratedProtocolMessageType('PeripheralMessage', (_message.Message,), {
  'DESCRIPTOR' : _PERIPHERALMESSAGE,
  '__module__' : 'jdiotprotocol_pb2'
  # @@protoc_insertion_point(class_scope:PeripheralMessage)
  })
_sym_db.RegisterMessage(PeripheralMessage)

PeripheralState = _reflection.GeneratedProtocolMessageType('PeripheralState', (_message.Message,), {
  'DESCRIPTOR' : _PERIPHERALSTATE,
  '__module__' : 'jdiotprotocol_pb2'
  # @@protoc_insertion_point(class_scope:PeripheralState)
  })
_sym_db.RegisterMessage(PeripheralState)

PeripheralStateBool = _reflection.GeneratedProtocolMessageType('PeripheralStateBool', (_message.Message,), {
  'DESCRIPTOR' : _PERIPHERALSTATEBOOL,
  '__module__' : 'jdiotprotocol_pb2'
  # @@protoc_insertion_point(class_scope:PeripheralStateBool)
  })
_sym_db.RegisterMessage(PeripheralStateBool)

PeripheralStateInt = _reflection.GeneratedProtocolMessageType('PeripheralStateInt', (_message.Message,), {
  'DESCRIPTOR' : _PERIPHERALSTATEINT,
  '__module__' : 'jdiotprotocol_pb2'
  # @@protoc_insertion_point(class_scope:PeripheralStateInt)
  })
_sym_db.RegisterMessage(PeripheralStateInt)

PeripheralStateString = _reflection.GeneratedProtocolMessageType('PeripheralStateString', (_message.Message,), {
  'DESCRIPTOR' : _PERIPHERALSTATESTRING,
  '__module__' : 'jdiotprotocol_pb2'
  # @@protoc_insertion_point(class_scope:PeripheralStateString)
  })
_sym_db.RegisterMessage(PeripheralStateString)

PeripheralStateBytes = _reflection.GeneratedProtocolMessageType('PeripheralStateBytes', (_message.Message,), {
  'DESCRIPTOR' : _PERIPHERALSTATEBYTES,
  '__module__' : 'jdiotprotocol_pb2'
  # @@protoc_insertion_point(class_scope:PeripheralStateBytes)
  })
_sym_db.RegisterMessage(PeripheralStateBytes)

PeripheralStateTagged = _reflection.GeneratedProtocolMessageType('PeripheralStateTagged', (_message.Message,), {
  'DESCRIPTOR' : _PERIPHERALSTATETAGGED,
  '__module__' : 'jdiotprotocol_pb2'
  # @@protoc_insertion_point(class_scope:PeripheralStateTagged)
  })
_sym_db.RegisterMessage(PeripheralStateTagged)

PeripheralAudio = _reflection.GeneratedProtocolMessageType('PeripheralAudio', (_message.Message,), {
  'DESCRIPTOR' : _PERIPHERALAUDIO,
  '__module__' : 'jdiotprotocol_pb2'
  # @@protoc_insertion_point(class_scope:PeripheralAudio)
  })
_sym_db.RegisterMessage(PeripheralAudio)

PeripheralVideo = _reflection.GeneratedProtocolMessageType('PeripheralVideo', (_message.Message,), {
  'DESCRIPTOR' : _PERIPHERALVIDEO,
  '__module__' : 'jdiotprotocol_pb2'
  # @@protoc_insertion_point(class_scope:PeripheralVideo)
  })
_sym_db.RegisterMessage(PeripheralVideo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _VIDEOTYPE._serialized_start=2039
  _VIDEOTYPE._serialized_end=2063
  _PERIPHERALDESCRIPTORTYPE._serialized_start=2065
  _PERIPHERALDESCRIPTORTYPE._serialized_end=2135
  _PERIPHERALTYPE._serialized_start=2137
  _PERIPHERALTYPE._serialized_end=2234
  _COMMANDTYPE._serialized_start=2237
  _COMMANDTYPE._serialized_end=2487
  _PERIPHERALCOMMANDTYPE._serialized_start=2489
  _PERIPHERALCOMMANDTYPE._serialized_end=2562
  _PSTATETYPE._serialized_start=2564
  _PSTATETYPE._serialized_end=2665
  _ERRORMSG._serialized_start=23
  _ERRORMSG._serialized_end=49
  _LOGMSG._serialized_start=51
  _LOGMSG._serialized_end=91
  _PACKET._serialized_start=93
  _PACKET._serialized_end=171
  _OPERATORREGISTERREQUEST._serialized_start=174
  _OPERATORREGISTERREQUEST._serialized_end=330
  _HARDWAREREGISTERREQUEST._serialized_start=333
  _HARDWAREREGISTERREQUEST._serialized_end=534
  _HARDWAREREGISTERRESPONSE._serialized_start=536
  _HARDWAREREGISTERRESPONSE._serialized_end=589
  _HARDWAREINFO._serialized_start=592
  _HARDWAREINFO._serialized_end=763
  _HARDWARESUBSCRIBE._serialized_start=765
  _HARDWARESUBSCRIBE._serialized_end=811
  _HARDWAREUNSUBSCRIBE._serialized_start=813
  _HARDWAREUNSUBSCRIBE._serialized_end=861
  _PERIPHERALADDED._serialized_start=863
  _PERIPHERALADDED._serialized_end=913
  _PERIPHERALREMOVED._serialized_start=915
  _PERIPHERALREMOVED._serialized_end=959
  _PERIPHERAL._serialized_start=962
  _PERIPHERAL._serialized_end=1115
  _PERIPHERALDESCRIPTOR._serialized_start=1117
  _PERIPHERALDESCRIPTOR._serialized_end=1239
  _PERIPHERALDESCRIPTORSTATEFUL._serialized_start=1241
  _PERIPHERALDESCRIPTORSTATEFUL._serialized_end=1362
  _PERIPHERALDESCRIPTORVIDEO._serialized_start=1364
  _PERIPHERALDESCRIPTORVIDEO._serialized_end=1462
  _PERIPHERALMESSAGE._serialized_start=1465
  _PERIPHERALMESSAGE._serialized_end=1617
  _PERIPHERALSTATE._serialized_start=1619
  _PERIPHERALSTATE._serialized_end=1683
  _PERIPHERALSTATEBOOL._serialized_start=1685
  _PERIPHERALSTATEBOOL._serialized_end=1721
  _PERIPHERALSTATEINT._serialized_start=1723
  _PERIPHERALSTATEINT._serialized_end=1758
  _PERIPHERALSTATESTRING._serialized_start=1760
  _PERIPHERALSTATESTRING._serialized_end=1798
  _PERIPHERALSTATEBYTES._serialized_start=1800
  _PERIPHERALSTATEBYTES._serialized_end=1837
  _PERIPHERALSTATETAGGED._serialized_start=1839
  _PERIPHERALSTATETAGGED._serialized_end=1890
  _PERIPHERALAUDIO._serialized_start=1892
  _PERIPHERALAUDIO._serialized_end=1924
  _PERIPHERALVIDEO._serialized_start=1926
  _PERIPHERALVIDEO._serialized_end=2037
# @@protoc_insertion_point(module_scope)
