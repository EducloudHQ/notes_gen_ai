import extensions_pb2 as _extensions_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class _Discontinuity(_message.Message):
    __slots__ = ["last_topic_sequence", "new_topic_sequence"]
    LAST_TOPIC_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    NEW_TOPIC_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    last_topic_sequence: int
    new_topic_sequence: int
    def __init__(self, last_topic_sequence: _Optional[int] = ..., new_topic_sequence: _Optional[int] = ...) -> None: ...

class _Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class _Heartbeat(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class _PublishRequest(_message.Message):
    __slots__ = ["cache_name", "topic", "value"]
    CACHE_NAME_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    cache_name: str
    topic: str
    value: _TopicValue
    def __init__(self, cache_name: _Optional[str] = ..., topic: _Optional[str] = ..., value: _Optional[_Union[_TopicValue, _Mapping]] = ...) -> None: ...

class _SubscriptionItem(_message.Message):
    __slots__ = ["discontinuity", "heartbeat", "item"]
    DISCONTINUITY_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    discontinuity: _Discontinuity
    heartbeat: _Heartbeat
    item: _TopicItem
    def __init__(self, item: _Optional[_Union[_TopicItem, _Mapping]] = ..., discontinuity: _Optional[_Union[_Discontinuity, _Mapping]] = ..., heartbeat: _Optional[_Union[_Heartbeat, _Mapping]] = ...) -> None: ...

class _SubscriptionRequest(_message.Message):
    __slots__ = ["cache_name", "resume_at_topic_sequence_number", "topic"]
    CACHE_NAME_FIELD_NUMBER: _ClassVar[int]
    RESUME_AT_TOPIC_SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    cache_name: str
    resume_at_topic_sequence_number: int
    topic: str
    def __init__(self, cache_name: _Optional[str] = ..., topic: _Optional[str] = ..., resume_at_topic_sequence_number: _Optional[int] = ...) -> None: ...

class _TopicItem(_message.Message):
    __slots__ = ["topic_sequence_number", "value"]
    TOPIC_SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    topic_sequence_number: int
    value: _TopicValue
    def __init__(self, topic_sequence_number: _Optional[int] = ..., value: _Optional[_Union[_TopicValue, _Mapping]] = ...) -> None: ...

class _TopicValue(_message.Message):
    __slots__ = ["binary", "text"]
    BINARY_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    binary: bytes
    text: str
    def __init__(self, text: _Optional[str] = ..., binary: _Optional[bytes] = ...) -> None: ...
