# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: demo.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'demo.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ndemo.proto\x12\x04\x64\x65mo\"-\n\x0eMessageRequest\x12\x0f\n\x07payload\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\"4\n\x0fMessageResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\x32\x8e\x01\n\x0b\x44\x65moService\x12<\n\x0bSendMessage\x12\x14.demo.MessageRequest\x1a\x15.demo.MessageResponse\"\x00\x12\x41\n\x0eStreamMessages\x12\x14.demo.MessageRequest\x1a\x15.demo.MessageResponse\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'demo_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MESSAGEREQUEST']._serialized_start=20
  _globals['_MESSAGEREQUEST']._serialized_end=65
  _globals['_MESSAGERESPONSE']._serialized_start=67
  _globals['_MESSAGERESPONSE']._serialized_end=119
  _globals['_DEMOSERVICE']._serialized_start=122
  _globals['_DEMOSERVICE']._serialized_end=264
# @@protoc_insertion_point(module_scope)
