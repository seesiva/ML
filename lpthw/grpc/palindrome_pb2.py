# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: palindrome.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='palindrome.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10palindrome.proto\"!\n\x10InputCheckString\x12\r\n\x05value\x18\x01 \x01(\t\"#\n\x12InputCheckResponse\x12\r\n\x05value\x18\x01 \x01(\x08\x32K\n\x11PalindromeChecker\x12\x36\n\x0cisPalindrome\x12\x11.InputCheckString\x1a\x13.InputCheckResponseb\x06proto3')
)




_INPUTCHECKSTRING = _descriptor.Descriptor(
  name='InputCheckString',
  full_name='InputCheckString',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='InputCheckString.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=20,
  serialized_end=53,
)


_INPUTCHECKRESPONSE = _descriptor.Descriptor(
  name='InputCheckResponse',
  full_name='InputCheckResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='InputCheckResponse.value', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=55,
  serialized_end=90,
)

DESCRIPTOR.message_types_by_name['InputCheckString'] = _INPUTCHECKSTRING
DESCRIPTOR.message_types_by_name['InputCheckResponse'] = _INPUTCHECKRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InputCheckString = _reflection.GeneratedProtocolMessageType('InputCheckString', (_message.Message,), dict(
  DESCRIPTOR = _INPUTCHECKSTRING,
  __module__ = 'palindrome_pb2'
  # @@protoc_insertion_point(class_scope:InputCheckString)
  ))
_sym_db.RegisterMessage(InputCheckString)

InputCheckResponse = _reflection.GeneratedProtocolMessageType('InputCheckResponse', (_message.Message,), dict(
  DESCRIPTOR = _INPUTCHECKRESPONSE,
  __module__ = 'palindrome_pb2'
  # @@protoc_insertion_point(class_scope:InputCheckResponse)
  ))
_sym_db.RegisterMessage(InputCheckResponse)



_PALINDROMECHECKER = _descriptor.ServiceDescriptor(
  name='PalindromeChecker',
  full_name='PalindromeChecker',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=92,
  serialized_end=167,
  methods=[
  _descriptor.MethodDescriptor(
    name='isPalindrome',
    full_name='PalindromeChecker.isPalindrome',
    index=0,
    containing_service=None,
    input_type=_INPUTCHECKSTRING,
    output_type=_INPUTCHECKRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PALINDROMECHECKER)

DESCRIPTOR.services_by_name['PalindromeChecker'] = _PALINDROMECHECKER

# @@protoc_insertion_point(module_scope)