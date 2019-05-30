# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: minetorch/rpc/grpc/minetorch.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='minetorch/rpc/grpc/minetorch.proto',
  package='minetorch',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\"minetorch/rpc/grpc/minetorch.proto\x12\tminetorch\"3\n\x10StandardResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"\xa8\x01\n\nHeyMessage\x12\x0f\n\x07ip_addr\x18\x01 \x01(\t\x12\x15\n\rexperiment_id\x18\x02 \x01(\x05\x12\x17\n\x0f\x65xperiment_name\x18\x03 \x01(\t\x12,\n\x06status\x18\x04 \x01(\x0e\x32\x1c.minetorch.HeyMessage.Status\"+\n\x06Status\x12\x08\n\x04IDLE\x10\x00\x12\x0c\n\x08TRAINING\x10\x01\x12\t\n\x05\x45RROR\x10\x02\"s\n\tYoMessage\x12\r\n\x05roger\x18\x01 \x01(\x08\x12-\n\x07\x63ommand\x18\x02 \x01(\x0e\x32\x1c.minetorch.YoMessage.Command\"(\n\x07\x43ommand\x12\t\n\x05TRAIN\x10\x00\x12\x08\n\x04HALT\x10\x01\x12\x08\n\x04KILL\x10\x02\"8\n\x03Log\x12\x15\n\rexperiment_id\x18\x01 \x01(\x05\x12\x0b\n\x03log\x18\x02 \x01(\t\x12\r\n\x05level\x18\x03 \x01(\t2}\n\tMinetorch\x12\x36\n\x05HeyYo\x12\x15.minetorch.HeyMessage\x1a\x14.minetorch.YoMessage\"\x00\x12\x38\n\x07SendLog\x12\x0e.minetorch.Log\x1a\x1b.minetorch.StandardResponse\"\x00\x62\x06proto3')
)



_HEYMESSAGE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='minetorch.HeyMessage.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IDLE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRAINING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=228,
  serialized_end=271,
)
_sym_db.RegisterEnumDescriptor(_HEYMESSAGE_STATUS)

_YOMESSAGE_COMMAND = _descriptor.EnumDescriptor(
  name='Command',
  full_name='minetorch.YoMessage.Command',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TRAIN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HALT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KILL', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=348,
  serialized_end=388,
)
_sym_db.RegisterEnumDescriptor(_YOMESSAGE_COMMAND)


_STANDARDRESPONSE = _descriptor.Descriptor(
  name='StandardResponse',
  full_name='minetorch.StandardResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='minetorch.StandardResponse.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='minetorch.StandardResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=100,
)


_HEYMESSAGE = _descriptor.Descriptor(
  name='HeyMessage',
  full_name='minetorch.HeyMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip_addr', full_name='minetorch.HeyMessage.ip_addr', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='experiment_id', full_name='minetorch.HeyMessage.experiment_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='experiment_name', full_name='minetorch.HeyMessage.experiment_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='minetorch.HeyMessage.status', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _HEYMESSAGE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=271,
)


_YOMESSAGE = _descriptor.Descriptor(
  name='YoMessage',
  full_name='minetorch.YoMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='roger', full_name='minetorch.YoMessage.roger', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='command', full_name='minetorch.YoMessage.command', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _YOMESSAGE_COMMAND,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=273,
  serialized_end=388,
)


_LOG = _descriptor.Descriptor(
  name='Log',
  full_name='minetorch.Log',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='experiment_id', full_name='minetorch.Log.experiment_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log', full_name='minetorch.Log.log', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='minetorch.Log.level', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=390,
  serialized_end=446,
)

_HEYMESSAGE.fields_by_name['status'].enum_type = _HEYMESSAGE_STATUS
_HEYMESSAGE_STATUS.containing_type = _HEYMESSAGE
_YOMESSAGE.fields_by_name['command'].enum_type = _YOMESSAGE_COMMAND
_YOMESSAGE_COMMAND.containing_type = _YOMESSAGE
DESCRIPTOR.message_types_by_name['StandardResponse'] = _STANDARDRESPONSE
DESCRIPTOR.message_types_by_name['HeyMessage'] = _HEYMESSAGE
DESCRIPTOR.message_types_by_name['YoMessage'] = _YOMESSAGE
DESCRIPTOR.message_types_by_name['Log'] = _LOG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StandardResponse = _reflection.GeneratedProtocolMessageType('StandardResponse', (_message.Message,), dict(
  DESCRIPTOR = _STANDARDRESPONSE,
  __module__ = 'minetorch.rpc.grpc.minetorch_pb2'
  # @@protoc_insertion_point(class_scope:minetorch.StandardResponse)
  ))
_sym_db.RegisterMessage(StandardResponse)

HeyMessage = _reflection.GeneratedProtocolMessageType('HeyMessage', (_message.Message,), dict(
  DESCRIPTOR = _HEYMESSAGE,
  __module__ = 'minetorch.rpc.grpc.minetorch_pb2'
  # @@protoc_insertion_point(class_scope:minetorch.HeyMessage)
  ))
_sym_db.RegisterMessage(HeyMessage)

YoMessage = _reflection.GeneratedProtocolMessageType('YoMessage', (_message.Message,), dict(
  DESCRIPTOR = _YOMESSAGE,
  __module__ = 'minetorch.rpc.grpc.minetorch_pb2'
  # @@protoc_insertion_point(class_scope:minetorch.YoMessage)
  ))
_sym_db.RegisterMessage(YoMessage)

Log = _reflection.GeneratedProtocolMessageType('Log', (_message.Message,), dict(
  DESCRIPTOR = _LOG,
  __module__ = 'minetorch.rpc.grpc.minetorch_pb2'
  # @@protoc_insertion_point(class_scope:minetorch.Log)
  ))
_sym_db.RegisterMessage(Log)



_MINETORCH = _descriptor.ServiceDescriptor(
  name='Minetorch',
  full_name='minetorch.Minetorch',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=448,
  serialized_end=573,
  methods=[
  _descriptor.MethodDescriptor(
    name='HeyYo',
    full_name='minetorch.Minetorch.HeyYo',
    index=0,
    containing_service=None,
    input_type=_HEYMESSAGE,
    output_type=_YOMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendLog',
    full_name='minetorch.Minetorch.SendLog',
    index=1,
    containing_service=None,
    input_type=_LOG,
    output_type=_STANDARDRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MINETORCH)

DESCRIPTOR.services_by_name['Minetorch'] = _MINETORCH

# @@protoc_insertion_point(module_scope)