from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor
NotRetryable: RetrySemantic
RETRY_SEMANTIC_FIELD_NUMBER: _ClassVar[int]
Retryable: RetrySemantic
retry_semantic: _descriptor.FieldDescriptor

class RetrySemantic(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
