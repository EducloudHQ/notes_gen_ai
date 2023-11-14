from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
Hit: ECacheResult
Invalid: ECacheResult
Miss: ECacheResult
Ok: ECacheResult

class _DeleteRequest(_message.Message):
    __slots__ = ["cache_key"]
    CACHE_KEY_FIELD_NUMBER: _ClassVar[int]
    cache_key: bytes
    def __init__(self, cache_key: _Optional[bytes] = ...) -> None: ...

class _DeleteResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class _DictionaryDeleteRequest(_message.Message):
    __slots__ = ["all", "dictionary_name", "some"]
    class All(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class Some(_message.Message):
        __slots__ = ["fields"]
        FIELDS_FIELD_NUMBER: _ClassVar[int]
        fields: _containers.RepeatedScalarFieldContainer[bytes]
        def __init__(self, fields: _Optional[_Iterable[bytes]] = ...) -> None: ...
    ALL_FIELD_NUMBER: _ClassVar[int]
    DICTIONARY_NAME_FIELD_NUMBER: _ClassVar[int]
    SOME_FIELD_NUMBER: _ClassVar[int]
    all: _DictionaryDeleteRequest.All
    dictionary_name: bytes
    some: _DictionaryDeleteRequest.Some
    def __init__(self, dictionary_name: _Optional[bytes] = ..., some: _Optional[_Union[_DictionaryDeleteRequest.Some, _Mapping]] = ..., all: _Optional[_Union[_DictionaryDeleteRequest.All, _Mapping]] = ...) -> None: ...

class _DictionaryDeleteResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class _DictionaryFetchRequest(_message.Message):
    __slots__ = ["dictionary_name"]
    DICTIONARY_NAME_FIELD_NUMBER: _ClassVar[int]
    dictionary_name: bytes
    def __init__(self, dictionary_name: _Optional[bytes] = ...) -> None: ...

class _DictionaryFetchResponse(_message.Message):
    __slots__ = ["found", "missing"]
    class _Found(_message.Message):
        __slots__ = ["items"]
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        items: _containers.RepeatedCompositeFieldContainer[_DictionaryFieldValuePair]
        def __init__(self, items: _Optional[_Iterable[_Union[_DictionaryFieldValuePair, _Mapping]]] = ...) -> None: ...
    class _Missing(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    FOUND_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELD_NUMBER: _ClassVar[int]
    found: _DictionaryFetchResponse._Found
    missing: _DictionaryFetchResponse._Missing
    def __init__(self, found: _Optional[_Union[_DictionaryFetchResponse._Found, _Mapping]] = ..., missing: _Optional[_Union[_DictionaryFetchResponse._Missing, _Mapping]] = ...) -> None: ...

class _DictionaryFieldValuePair(_message.Message):
    __slots__ = ["field", "value"]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    field: bytes
    value: bytes
    def __init__(self, field: _Optional[bytes] = ..., value: _Optional[bytes] = ...) -> None: ...

class _DictionaryGetRequest(_message.Message):
    __slots__ = ["dictionary_name", "fields"]
    DICTIONARY_NAME_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    dictionary_name: bytes
    fields: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, dictionary_name: _Optional[bytes] = ..., fields: _Optional[_Iterable[bytes]] = ...) -> None: ...

class _DictionaryGetResponse(_message.Message):
    __slots__ = ["found", "missing"]
    class _DictionaryGetResponsePart(_message.Message):
        __slots__ = ["cache_body", "result"]
        CACHE_BODY_FIELD_NUMBER: _ClassVar[int]
        RESULT_FIELD_NUMBER: _ClassVar[int]
        cache_body: bytes
        result: ECacheResult
        def __init__(self, result: _Optional[_Union[ECacheResult, str]] = ..., cache_body: _Optional[bytes] = ...) -> None: ...
    class _Found(_message.Message):
        __slots__ = ["items"]
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        items: _containers.RepeatedCompositeFieldContainer[_DictionaryGetResponse._DictionaryGetResponsePart]
        def __init__(self, items: _Optional[_Iterable[_Union[_DictionaryGetResponse._DictionaryGetResponsePart, _Mapping]]] = ...) -> None: ...
    class _Missing(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    FOUND_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELD_NUMBER: _ClassVar[int]
    found: _DictionaryGetResponse._Found
    missing: _DictionaryGetResponse._Missing
    def __init__(self, found: _Optional[_Union[_DictionaryGetResponse._Found, _Mapping]] = ..., missing: _Optional[_Union[_DictionaryGetResponse._Missing, _Mapping]] = ...) -> None: ...

class _DictionaryIncrementRequest(_message.Message):
    __slots__ = ["amount", "dictionary_name", "field", "refresh_ttl", "ttl_milliseconds"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    DICTIONARY_NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TTL_FIELD_NUMBER: _ClassVar[int]
    TTL_MILLISECONDS_FIELD_NUMBER: _ClassVar[int]
    amount: int
    dictionary_name: bytes
    field: bytes
    refresh_ttl: bool
    ttl_milliseconds: int
    def __init__(self, dictionary_name: _Optional[bytes] = ..., field: _Optional[bytes] = ..., amount: _Optional[int] = ..., ttl_milliseconds: _Optional[int] = ..., refresh_ttl: bool = ...) -> None: ...

class _DictionaryIncrementResponse(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class _DictionaryLengthRequest(_message.Message):
    __slots__ = ["dictionary_name"]
    DICTIONARY_NAME_FIELD_NUMBER: _ClassVar[int]
    dictionary_name: bytes
    def __init__(self, dictionary_name: _Optional[bytes] = ...) -> None: ...

class _DictionaryLengthResponse(_message.Message):
    __slots__ = ["found", "missing"]
    class _Found(_message.Message):
        __slots__ = ["length"]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        length: int
        def __init__(self, length: _Optional[int] = ...) -> None: ...
    class _Missing(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    FOUND_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELD_NUMBER: _ClassVar[int]
    found: _DictionaryLengthResponse._Found
    missing: _DictionaryLengthResponse._Missing
    def __init__(self, found: _Optional[_Union[_DictionaryLengthResponse._Found, _Mapping]] = ..., missing: _Optional[_Union[_DictionaryLengthResponse._Missing, _Mapping]] = ...) -> None: ...

class _DictionarySetRequest(_message.Message):
    __slots__ = ["dictionary_name", "items", "refresh_ttl", "ttl_milliseconds"]
    DICTIONARY_NAME_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TTL_FIELD_NUMBER: _ClassVar[int]
    TTL_MILLISECONDS_FIELD_NUMBER: _ClassVar[int]
    dictionary_name: bytes
    items: _containers.RepeatedCompositeFieldContainer[_DictionaryFieldValuePair]
    refresh_ttl: bool
    ttl_milliseconds: int
    def __init__(self, dictionary_name: _Optional[bytes] = ..., items: _Optional[_Iterable[_Union[_DictionaryFieldValuePair, _Mapping]]] = ..., ttl_milliseconds: _Optional[int] = ..., refresh_ttl: bool = ...) -> None: ...

class _DictionarySetResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class _GetRequest(_message.Message):
    __slots__ = ["cache_key"]
    CACHE_KEY_FIELD_NUMBER: _ClassVar[int]
    cache_key: bytes
    def __init__(self, cache_key: _Optional[bytes] = ...) -> None: ...

class _GetResponse(_message.Message):
    __slots__ = ["cache_body", "message", "result"]
    CACHE_BODY_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    cache_body: bytes
    message: str
    result: ECacheResult
    def __init__(self, result: _Optional[_Union[ECacheResult, str]] = ..., cache_body: _Optional[bytes] = ..., message: _Optional[str] = ...) -> None: ...

class _IncrementRequest(_message.Message):
    __slots__ = ["amount", "cache_key", "ttl_milliseconds"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CACHE_KEY_FIELD_NUMBER: _ClassVar[int]
    TTL_MILLISECONDS_FIELD_NUMBER: _ClassVar[int]
    amount: int
    cache_key: bytes
    ttl_milliseconds: int
    def __init__(self, cache_key: _Optional[bytes] = ..., amount: _Optional[int] = ..., ttl_milliseconds: _Optional[int] = ...) -> None: ...

class _IncrementResponse(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class _ItemGetTtlRequest(_message.Message):
    __slots__ = ["cache_key"]
    CACHE_KEY_FIELD_NUMBER: _ClassVar[int]
    cache_key: bytes
    def __init__(self, cache_key: _Optional[bytes] = ...) -> None: ...

class _ItemGetTtlResponse(_message.Message):
    __slots__ = ["found", "missing"]
    class _Found(_message.Message):
        __slots__ = ["remaining_ttl_millis"]
        REMAINING_TTL_MILLIS_FIELD_NUMBER: _ClassVar[int]
        remaining_ttl_millis: int
        def __init__(self, remaining_ttl_millis: _Optional[int] = ...) -> None: ...
    class _Missing(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    FOUND_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELD_NUMBER: _ClassVar[int]
    found: _ItemGetTtlResponse._Found
    missing: _ItemGetTtlResponse._Missing
    def __init__(self, found: _Optional[_Union[_ItemGetTtlResponse._Found, _Mapping]] = ..., missing: _Optional[_Union[_ItemGetTtlResponse._Missing, _Mapping]] = ...) -> None: ...

class _ItemGetTypeRequest(_message.Message):
    __slots__ = ["cache_key"]
    CACHE_KEY_FIELD_NUMBER: _ClassVar[int]
    cache_key: bytes
    def __init__(self, cache_key: _Optional[bytes] = ...) -> None: ...

class _ItemGetTypeResponse(_message.Message):
    __slots__ = ["found", "missing"]
    class ItemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class _Found(_message.Message):
        __slots__ = ["item_type"]
        ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
        item_type: _ItemGetTypeResponse.ItemType
        def __init__(self, item_type: _Optional[_Union[_ItemGetTypeResponse.ItemType, str]] = ...) -> None: ...
    class _Missing(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    DICTIONARY: _ItemGetTypeResponse.ItemType
    FOUND_FIELD_NUMBER: _ClassVar[int]
    LIST: _ItemGetTypeResponse.ItemType
    MISSING_FIELD_NUMBER: _ClassVar[int]
    SCALAR: _ItemGetTypeResponse.ItemType
    SET: _ItemGetTypeResponse.ItemType
    SORTED_SET: _ItemGetTypeResponse.ItemType
    found: _ItemGetTypeResponse._Found
    missing: _ItemGetTypeResponse._Missing
    def __init__(self, found: _Optional[_Union[_ItemGetTypeResponse._Found, _Mapping]] = ..., missing: _Optional[_Union[_ItemGetTypeResponse._Missing, _Mapping]] = ...) -> None: ...

class _KeysExistRequest(_message.Message):
    __slots__ = ["cache_keys"]
    CACHE_KEYS_FIELD_NUMBER: _ClassVar[int]
    cache_keys: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, cache_keys: _Optional[_Iterable[bytes]] = ...) -> None: ...

class _KeysExistResponse(_message.Message):
    __slots__ = ["exists"]
    EXISTS_FIELD_NUMBER: _ClassVar[int]
    exists: _containers.RepeatedScalarFieldContainer[bool]
    def __init__(self, exists: _Optional[_Iterable[bool]] = ...) -> None: ...

class _ListConcatenateBackRequest(_message.Message):
    __slots__ = ["list_name", "refresh_ttl", "truncate_front_to_size", "ttl_milliseconds", "values"]
    LIST_NAME_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TTL_FIELD_NUMBER: _ClassVar[int]
    TRUNCATE_FRONT_TO_SIZE_FIELD_NUMBER: _ClassVar[int]
    TTL_MILLISECONDS_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    list_name: bytes
    refresh_ttl: bool
    truncate_front_to_size: int
    ttl_milliseconds: int
    values: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, list_name: _Optional[bytes] = ..., values: _Optional[_Iterable[bytes]] = ..., ttl_milliseconds: _Optional[int] = ..., refresh_ttl: bool = ..., truncate_front_to_size: _Optional[int] = ...) -> None: ...

class _ListConcatenateBackResponse(_message.Message):
    __slots__ = ["list_length"]
    LIST_LENGTH_FIELD_NUMBER: _ClassVar[int]
    list_length: int
    def __init__(self, list_length: _Optional[int] = ...) -> None: ...

class _ListConcatenateFrontRequest(_message.Message):
    __slots__ = ["list_name", "refresh_ttl", "truncate_back_to_size", "ttl_milliseconds", "values"]
    LIST_NAME_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TTL_FIELD_NUMBER: _ClassVar[int]
    TRUNCATE_BACK_TO_SIZE_FIELD_NUMBER: _ClassVar[int]
    TTL_MILLISECONDS_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    list_name: bytes
    refresh_ttl: bool
    truncate_back_to_size: int
    ttl_milliseconds: int
    values: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, list_name: _Optional[bytes] = ..., values: _Optional[_Iterable[bytes]] = ..., ttl_milliseconds: _Optional[int] = ..., refresh_ttl: bool = ..., truncate_back_to_size: _Optional[int] = ...) -> None: ...

class _ListConcatenateFrontResponse(_message.Message):
    __slots__ = ["list_length"]
    LIST_LENGTH_FIELD_NUMBER: _ClassVar[int]
    list_length: int
    def __init__(self, list_length: _Optional[int] = ...) -> None: ...

class _ListEraseRequest(_message.Message):
    __slots__ = ["all", "list_name", "some"]
    class _All(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class _ListRanges(_message.Message):
        __slots__ = ["ranges"]
        RANGES_FIELD_NUMBER: _ClassVar[int]
        ranges: _containers.RepeatedCompositeFieldContainer[_ListRange]
        def __init__(self, ranges: _Optional[_Iterable[_Union[_ListRange, _Mapping]]] = ...) -> None: ...
    ALL_FIELD_NUMBER: _ClassVar[int]
    LIST_NAME_FIELD_NUMBER: _ClassVar[int]
    SOME_FIELD_NUMBER: _ClassVar[int]
    all: _ListEraseRequest._All
    list_name: bytes
    some: _ListEraseRequest._ListRanges
    def __init__(self, list_name: _Optional[bytes] = ..., some: _Optional[_Union[_ListEraseRequest._ListRanges, _Mapping]] = ..., all: _Optional[_Union[_ListEraseRequest._All, _Mapping]] = ...) -> None: ...

class _ListEraseResponse(_message.Message):
    __slots__ = ["found", "missing"]
    class _Found(_message.Message):
        __slots__ = ["list_length"]
        LIST_LENGTH_FIELD_NUMBER: _ClassVar[int]
        list_length: int
        def __init__(self, list_length: _Optional[int] = ...) -> None: ...
    class _Missing(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    FOUND_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELD_NUMBER: _ClassVar[int]
    found: _ListEraseResponse._Found
    missing: _ListEraseResponse._Missing
    def __init__(self, found: _Optional[_Union[_ListEraseResponse._Found, _Mapping]] = ..., missing: _Optional[_Union[_ListEraseResponse._Missing, _Mapping]] = ...) -> None: ...

class _ListFetchRequest(_message.Message):
    __slots__ = ["exclusive_end", "inclusive_start", "list_name", "unbounded_end", "unbounded_start"]
    EXCLUSIVE_END_FIELD_NUMBER: _ClassVar[int]
    INCLUSIVE_START_FIELD_NUMBER: _ClassVar[int]
    LIST_NAME_FIELD_NUMBER: _ClassVar[int]
    UNBOUNDED_END_FIELD_NUMBER: _ClassVar[int]
    UNBOUNDED_START_FIELD_NUMBER: _ClassVar[int]
    exclusive_end: int
    inclusive_start: int
    list_name: bytes
    unbounded_end: _Unbounded
    unbounded_start: _Unbounded
    def __init__(self, list_name: _Optional[bytes] = ..., unbounded_start: _Optional[_Union[_Unbounded, _Mapping]] = ..., inclusive_start: _Optional[int] = ..., unbounded_end: _Optional[_Union[_Unbounded, _Mapping]] = ..., exclusive_end: _Optional[int] = ...) -> None: ...

class _ListFetchResponse(_message.Message):
    __slots__ = ["found", "missing"]
    class _Found(_message.Message):
        __slots__ = ["values"]
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedScalarFieldContainer[bytes]
        def __init__(self, values: _Optional[_Iterable[bytes]] = ...) -> None: ...
    class _Missing(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    FOUND_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELD_NUMBER: _ClassVar[int]
    found: _ListFetchResponse._Found
    missing: _ListFetchResponse._Missing
    def __init__(self, found: _Optional[_Union[_ListFetchResponse._Found, _Mapping]] = ..., missing: _Optional[_Union[_ListFetchResponse._Missing, _Mapping]] = ...) -> None: ...

class _ListLengthRequest(_message.Message):
    __slots__ = ["list_name"]
    LIST_NAME_FIELD_NUMBER: _ClassVar[int]
    list_name: bytes
    def __init__(self, list_name: _Optional[bytes] = ...) -> None: ...

class _ListLengthResponse(_message.Message):
    __slots__ = ["found", "missing"]
    class _Found(_message.Message):
        __slots__ = ["length"]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        length: int
        def __init__(self, length: _Optional[int] = ...) -> None: ...
    class _Missing(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    FOUND_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELD_NUMBER: _ClassVar[int]
    found: _ListLengthResponse._Found
    missing: _ListLengthResponse._Missing
    def __init__(self, found: _Optional[_Union[_ListLengthResponse._Found, _Mapping]] = ..., missing: _Optional[_Union[_ListLengthResponse._Missing, _Mapping]] = ...) -> None: ...

class _ListPopBackRequest(_message.Message):
    __slots__ = ["list_name"]
    LIST_NAME_FIELD_NUMBER: _ClassVar[int]
    list_name: bytes
    def __init__(self, list_name: _Optional[bytes] = ...) -> None: ...

class _ListPopBackResponse(_message.Message):
    __slots__ = ["found", "missing"]
    class _Found(_message.Message):
        __slots__ = ["back", "list_length"]
        BACK_FIELD_NUMBER: _ClassVar[int]
        LIST_LENGTH_FIELD_NUMBER: _ClassVar[int]
        back: bytes
        list_length: int
        def __init__(self, back: _Optional[bytes] = ..., list_length: _Optional[int] = ...) -> None: ...
    class _Missing(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    FOUND_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELD_NUMBER: _ClassVar[int]
    found: _ListPopBackResponse._Found
    missing: _ListPopBackResponse._Missing
    def __init__(self, found: _Optional[_Union[_ListPopBackResponse._Found, _Mapping]] = ..., missing: _Optional[_Union[_ListPopBackResponse._Missing, _Mapping]] = ...) -> None: ...

class _ListPopFrontRequest(_message.Message):
    __slots__ = ["list_name"]
    LIST_NAME_FIELD_NUMBER: _ClassVar[int]
    list_name: bytes
    def __init__(self, list_name: _Optional[bytes] = ...) -> None: ...

class _ListPopFrontResponse(_message.Message):
    __slots__ = ["found", "missing"]
    class _Found(_message.Message):
        __slots__ = ["front", "list_length"]
        FRONT_FIELD_NUMBER: _ClassVar[int]
        LIST_LENGTH_FIELD_NUMBER: _ClassVar[int]
        front: bytes
        list_length: int
        def __init__(self, front: _Optional[bytes] = ..., list_length: _Optional[int] = ...) -> None: ...
    class _Missing(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    FOUND_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELD_NUMBER: _ClassVar[int]
    found: _ListPopFrontResponse._Found
    missing: _ListPopFrontResponse._Missing
    def __init__(self, found: _Optional[_Union[_ListPopFrontResponse._Found, _Mapping]] = ..., missing: _Optional[_Union[_ListPopFrontResponse._Missing, _Mapping]] = ...) -> None: ...

class _ListPushBackRequest(_message.Message):
    __slots__ = ["list_name", "refresh_ttl", "truncate_front_to_size", "ttl_milliseconds", "value"]
    LIST_NAME_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TTL_FIELD_NUMBER: _ClassVar[int]
    TRUNCATE_FRONT_TO_SIZE_FIELD_NUMBER: _ClassVar[int]
    TTL_MILLISECONDS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    list_name: bytes
    refresh_ttl: bool
    truncate_front_to_size: int
    ttl_milliseconds: int
    value: bytes
    def __init__(self, list_name: _Optional[bytes] = ..., value: _Optional[bytes] = ..., ttl_milliseconds: _Optional[int] = ..., refresh_ttl: bool = ..., truncate_front_to_size: _Optional[int] = ...) -> None: ...

class _ListPushBackResponse(_message.Message):
    __slots__ = ["list_length"]
    LIST_LENGTH_FIELD_NUMBER: _ClassVar[int]
    list_length: int
    def __init__(self, list_length: _Optional[int] = ...) -> None: ...

class _ListPushFrontRequest(_message.Message):
    __slots__ = ["list_name", "refresh_ttl", "truncate_back_to_size", "ttl_milliseconds", "value"]
    LIST_NAME_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TTL_FIELD_NUMBER: _ClassVar[int]
    TRUNCATE_BACK_TO_SIZE_FIELD_NUMBER: _ClassVar[int]
    TTL_MILLISECONDS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    list_name: bytes
    refresh_ttl: bool
    truncate_back_to_size: int
    ttl_milliseconds: int
    value: bytes
    def __init__(self, list_name: _Optional[bytes] = ..., value: _Optional[bytes] = ..., ttl_milliseconds: _Optional[int] = ..., refresh_ttl: bool = ..., truncate_back_to_size: _Optional[int] = ...) -> None: ...

class _ListPushFrontResponse(_message.Message):
    __slots__ = ["list_length"]
    LIST_LENGTH_FIELD_NUMBER: _ClassVar[int]
    list_length: int
    def __init__(self, list_length: _Optional[int] = ...) -> None: ...

class _ListRange(_message.Message):
    __slots__ = ["begin_index", "count"]
    BEGIN_INDEX_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    begin_index: int
    count: int
    def __init__(self, begin_index: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...

class _ListRemoveRequest(_message.Message):
    __slots__ = ["all_elements_with_value", "list_name"]
    ALL_ELEMENTS_WITH_VALUE_FIELD_NUMBER: _ClassVar[int]
    LIST_NAME_FIELD_NUMBER: _ClassVar[int]
    all_elements_with_value: bytes
    list_name: bytes
    def __init__(self, list_name: _Optional[bytes] = ..., all_elements_with_value: _Optional[bytes] = ...) -> None: ...

class _ListRemoveResponse(_message.Message):
    __slots__ = ["found", "missing"]
    class _Found(_message.Message):
        __slots__ = ["list_length"]
        LIST_LENGTH_FIELD_NUMBER: _ClassVar[int]
        list_length: int
        def __init__(self, list_length: _Optional[int] = ...) -> None: ...
    class _Missing(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    FOUND_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELD_NUMBER: _ClassVar[int]
    found: _ListRemoveResponse._Found
    missing: _ListRemoveResponse._Missing
    def __init__(self, found: _Optional[_Union[_ListRemoveResponse._Found, _Mapping]] = ..., missing: _Optional[_Union[_ListRemoveResponse._Missing, _Mapping]] = ...) -> None: ...

class _ListRetainRequest(_message.Message):
    __slots__ = ["exclusive_end", "inclusive_start", "list_name", "refresh_ttl", "ttl_milliseconds", "unbounded_end", "unbounded_start"]
    EXCLUSIVE_END_FIELD_NUMBER: _ClassVar[int]
    INCLUSIVE_START_FIELD_NUMBER: _ClassVar[int]
    LIST_NAME_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TTL_FIELD_NUMBER: _ClassVar[int]
    TTL_MILLISECONDS_FIELD_NUMBER: _ClassVar[int]
    UNBOUNDED_END_FIELD_NUMBER: _ClassVar[int]
    UNBOUNDED_START_FIELD_NUMBER: _ClassVar[int]
    exclusive_end: int
    inclusive_start: int
    list_name: bytes
    refresh_ttl: bool
    ttl_milliseconds: int
    unbounded_end: _Unbounded
    unbounded_start: _Unbounded
    def __init__(self, list_name: _Optional[bytes] = ..., unbounded_start: _Optional[_Union[_Unbounded, _Mapping]] = ..., inclusive_start: _Optional[int] = ..., unbounded_end: _Optional[_Union[_Unbounded, _Mapping]] = ..., exclusive_end: _Optional[int] = ..., ttl_milliseconds: _Optional[int] = ..., refresh_ttl: bool = ...) -> None: ...

class _ListRetainResponse(_message.Message):
    __slots__ = ["found", "missing"]
    class _Found(_message.Message):
        __slots__ = ["list_length"]
        LIST_LENGTH_FIELD_NUMBER: _ClassVar[int]
        list_length: int
        def __init__(self, list_length: _Optional[int] = ...) -> None: ...
    class _Missing(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    FOUND_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELD_NUMBER: _ClassVar[int]
    found: _ListRetainResponse._Found
    missing: _ListRetainResponse._Missing
    def __init__(self, found: _Optional[_Union[_ListRetainResponse._Found, _Mapping]] = ..., missing: _Optional[_Union[_ListRetainResponse._Missing, _Mapping]] = ...) -> None: ...

class _SetContainsRequest(_message.Message):
    __slots__ = ["elements", "set_name"]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    SET_NAME_FIELD_NUMBER: _ClassVar[int]
    elements: _containers.RepeatedScalarFieldContainer[bytes]
    set_name: bytes
    def __init__(self, set_name: _Optional[bytes] = ..., elements: _Optional[_Iterable[bytes]] = ...) -> None: ...

class _SetContainsResponse(_message.Message):
    __slots__ = ["found", "missing"]
    class _Found(_message.Message):
        __slots__ = ["contains"]
        CONTAINS_FIELD_NUMBER: _ClassVar[int]
        contains: _containers.RepeatedScalarFieldContainer[bool]
        def __init__(self, contains: _Optional[_Iterable[bool]] = ...) -> None: ...
    class _Missing(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    FOUND_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELD_NUMBER: _ClassVar[int]
    found: _SetContainsResponse._Found
    missing: _SetContainsResponse._Missing
    def __init__(self, found: _Optional[_Union[_SetContainsResponse._Found, _Mapping]] = ..., missing: _Optional[_Union[_SetContainsResponse._Missing, _Mapping]] = ...) -> None: ...

class _SetDifferenceRequest(_message.Message):
    __slots__ = ["minuend", "set_name", "subtrahend"]
    class _Minuend(_message.Message):
        __slots__ = ["elements"]
        ELEMENTS_FIELD_NUMBER: _ClassVar[int]
        elements: _containers.RepeatedScalarFieldContainer[bytes]
        def __init__(self, elements: _Optional[_Iterable[bytes]] = ...) -> None: ...
    class _Subtrahend(_message.Message):
        __slots__ = ["identity", "set"]
        class _Identity(_message.Message):
            __slots__ = []
            def __init__(self) -> None: ...
        class _Set(_message.Message):
            __slots__ = ["elements"]
            ELEMENTS_FIELD_NUMBER: _ClassVar[int]
            elements: _containers.RepeatedScalarFieldContainer[bytes]
            def __init__(self, elements: _Optional[_Iterable[bytes]] = ...) -> None: ...
        IDENTITY_FIELD_NUMBER: _ClassVar[int]
        SET_FIELD_NUMBER: _ClassVar[int]
        identity: _SetDifferenceRequest._Subtrahend._Identity
        set: _SetDifferenceRequest._Subtrahend._Set
        def __init__(self, set: _Optional[_Union[_SetDifferenceRequest._Subtrahend._Set, _Mapping]] = ..., identity: _Optional[_Union[_SetDifferenceRequest._Subtrahend._Identity, _Mapping]] = ...) -> None: ...
    MINUEND_FIELD_NUMBER: _ClassVar[int]
    SET_NAME_FIELD_NUMBER: _ClassVar[int]
    SUBTRAHEND_FIELD_NUMBER: _ClassVar[int]
    minuend: _SetDifferenceRequest._Minuend
    set_name: bytes
    subtrahend: _SetDifferenceRequest._Subtrahend
    def __init__(self, set_name: _Optional[bytes] = ..., minuend: _Optional[_Union[_SetDifferenceRequest._Minuend, _Mapping]] = ..., subtrahend: _Optional[_Union[_SetDifferenceRequest._Subtrahend, _Mapping]] = ...) -> None: ...

class _SetDifferenceResponse(_message.Message):
    __slots__ = ["found", "missing"]
    class _Found(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class _Missing(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    FOUND_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELD_NUMBER: _ClassVar[int]
    found: _SetDifferenceResponse._Found
    missing: _SetDifferenceResponse._Missing
    def __init__(self, found: _Optional[_Union[_SetDifferenceResponse._Found, _Mapping]] = ..., missing: _Optional[_Union[_SetDifferenceResponse._Missing, _Mapping]] = ...) -> None: ...

class _SetFetchRequest(_message.Message):
    __slots__ = ["set_name"]
    SET_NAME_FIELD_NUMBER: _ClassVar[int]
    set_name: bytes
    def __init__(self, set_name: _Optional[bytes] = ...) -> None: ...

class _SetFetchResponse(_message.Message):
    __slots__ = ["found", "missing"]
    class _Found(_message.Message):
        __slots__ = ["elements"]
        ELEMENTS_FIELD_NUMBER: _ClassVar[int]
        elements: _containers.RepeatedScalarFieldContainer[bytes]
        def __init__(self, elements: _Optional[_Iterable[bytes]] = ...) -> None: ...
    class _Missing(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    FOUND_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELD_NUMBER: _ClassVar[int]
    found: _SetFetchResponse._Found
    missing: _SetFetchResponse._Missing
    def __init__(self, found: _Optional[_Union[_SetFetchResponse._Found, _Mapping]] = ..., missing: _Optional[_Union[_SetFetchResponse._Missing, _Mapping]] = ...) -> None: ...

class _SetIfNotExistsRequest(_message.Message):
    __slots__ = ["cache_body", "cache_key", "ttl_milliseconds"]
    CACHE_BODY_FIELD_NUMBER: _ClassVar[int]
    CACHE_KEY_FIELD_NUMBER: _ClassVar[int]
    TTL_MILLISECONDS_FIELD_NUMBER: _ClassVar[int]
    cache_body: bytes
    cache_key: bytes
    ttl_milliseconds: int
    def __init__(self, cache_key: _Optional[bytes] = ..., cache_body: _Optional[bytes] = ..., ttl_milliseconds: _Optional[int] = ...) -> None: ...

class _SetIfNotExistsResponse(_message.Message):
    __slots__ = ["not_stored", "stored"]
    class _NotStored(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class _Stored(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    NOT_STORED_FIELD_NUMBER: _ClassVar[int]
    STORED_FIELD_NUMBER: _ClassVar[int]
    not_stored: _SetIfNotExistsResponse._NotStored
    stored: _SetIfNotExistsResponse._Stored
    def __init__(self, stored: _Optional[_Union[_SetIfNotExistsResponse._Stored, _Mapping]] = ..., not_stored: _Optional[_Union[_SetIfNotExistsResponse._NotStored, _Mapping]] = ...) -> None: ...

class _SetLengthRequest(_message.Message):
    __slots__ = ["set_name"]
    SET_NAME_FIELD_NUMBER: _ClassVar[int]
    set_name: bytes
    def __init__(self, set_name: _Optional[bytes] = ...) -> None: ...

class _SetLengthResponse(_message.Message):
    __slots__ = ["found", "missing"]
    class _Found(_message.Message):
        __slots__ = ["length"]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        length: int
        def __init__(self, length: _Optional[int] = ...) -> None: ...
    class _Missing(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    FOUND_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELD_NUMBER: _ClassVar[int]
    found: _SetLengthResponse._Found
    missing: _SetLengthResponse._Missing
    def __init__(self, found: _Optional[_Union[_SetLengthResponse._Found, _Mapping]] = ..., missing: _Optional[_Union[_SetLengthResponse._Missing, _Mapping]] = ...) -> None: ...

class _SetPopRequest(_message.Message):
    __slots__ = ["count", "set_name"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    SET_NAME_FIELD_NUMBER: _ClassVar[int]
    count: int
    set_name: bytes
    def __init__(self, set_name: _Optional[bytes] = ..., count: _Optional[int] = ...) -> None: ...

class _SetPopResponse(_message.Message):
    __slots__ = ["found", "missing"]
    class _Found(_message.Message):
        __slots__ = ["elements"]
        ELEMENTS_FIELD_NUMBER: _ClassVar[int]
        elements: _containers.RepeatedScalarFieldContainer[bytes]
        def __init__(self, elements: _Optional[_Iterable[bytes]] = ...) -> None: ...
    class _Missing(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    FOUND_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELD_NUMBER: _ClassVar[int]
    found: _SetPopResponse._Found
    missing: _SetPopResponse._Missing
    def __init__(self, found: _Optional[_Union[_SetPopResponse._Found, _Mapping]] = ..., missing: _Optional[_Union[_SetPopResponse._Missing, _Mapping]] = ...) -> None: ...

class _SetRequest(_message.Message):
    __slots__ = ["cache_body", "cache_key", "ttl_milliseconds"]
    CACHE_BODY_FIELD_NUMBER: _ClassVar[int]
    CACHE_KEY_FIELD_NUMBER: _ClassVar[int]
    TTL_MILLISECONDS_FIELD_NUMBER: _ClassVar[int]
    cache_body: bytes
    cache_key: bytes
    ttl_milliseconds: int
    def __init__(self, cache_key: _Optional[bytes] = ..., cache_body: _Optional[bytes] = ..., ttl_milliseconds: _Optional[int] = ...) -> None: ...

class _SetResponse(_message.Message):
    __slots__ = ["message", "result"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    message: str
    result: ECacheResult
    def __init__(self, result: _Optional[_Union[ECacheResult, str]] = ..., message: _Optional[str] = ...) -> None: ...

class _SetUnionRequest(_message.Message):
    __slots__ = ["elements", "refresh_ttl", "set_name", "ttl_milliseconds"]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TTL_FIELD_NUMBER: _ClassVar[int]
    SET_NAME_FIELD_NUMBER: _ClassVar[int]
    TTL_MILLISECONDS_FIELD_NUMBER: _ClassVar[int]
    elements: _containers.RepeatedScalarFieldContainer[bytes]
    refresh_ttl: bool
    set_name: bytes
    ttl_milliseconds: int
    def __init__(self, set_name: _Optional[bytes] = ..., elements: _Optional[_Iterable[bytes]] = ..., ttl_milliseconds: _Optional[int] = ..., refresh_ttl: bool = ...) -> None: ...

class _SetUnionResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class _SortedSetElement(_message.Message):
    __slots__ = ["score", "value"]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    score: float
    value: bytes
    def __init__(self, value: _Optional[bytes] = ..., score: _Optional[float] = ...) -> None: ...

class _SortedSetFetchRequest(_message.Message):
    __slots__ = ["by_index", "by_score", "order", "set_name", "with_scores"]
    class Order(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class _ByIndex(_message.Message):
        __slots__ = ["exclusive_end_index", "inclusive_start_index", "unbounded_end", "unbounded_start"]
        EXCLUSIVE_END_INDEX_FIELD_NUMBER: _ClassVar[int]
        INCLUSIVE_START_INDEX_FIELD_NUMBER: _ClassVar[int]
        UNBOUNDED_END_FIELD_NUMBER: _ClassVar[int]
        UNBOUNDED_START_FIELD_NUMBER: _ClassVar[int]
        exclusive_end_index: int
        inclusive_start_index: int
        unbounded_end: _Unbounded
        unbounded_start: _Unbounded
        def __init__(self, unbounded_start: _Optional[_Union[_Unbounded, _Mapping]] = ..., inclusive_start_index: _Optional[int] = ..., unbounded_end: _Optional[_Union[_Unbounded, _Mapping]] = ..., exclusive_end_index: _Optional[int] = ...) -> None: ...
    class _ByScore(_message.Message):
        __slots__ = ["count", "max_score", "min_score", "offset", "unbounded_max", "unbounded_min"]
        class _Score(_message.Message):
            __slots__ = ["exclusive", "score"]
            EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
            SCORE_FIELD_NUMBER: _ClassVar[int]
            exclusive: bool
            score: float
            def __init__(self, score: _Optional[float] = ..., exclusive: bool = ...) -> None: ...
        COUNT_FIELD_NUMBER: _ClassVar[int]
        MAX_SCORE_FIELD_NUMBER: _ClassVar[int]
        MIN_SCORE_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        UNBOUNDED_MAX_FIELD_NUMBER: _ClassVar[int]
        UNBOUNDED_MIN_FIELD_NUMBER: _ClassVar[int]
        count: int
        max_score: _SortedSetFetchRequest._ByScore._Score
        min_score: _SortedSetFetchRequest._ByScore._Score
        offset: int
        unbounded_max: _Unbounded
        unbounded_min: _Unbounded
        def __init__(self, unbounded_min: _Optional[_Union[_Unbounded, _Mapping]] = ..., min_score: _Optional[_Union[_SortedSetFetchRequest._ByScore._Score, _Mapping]] = ..., unbounded_max: _Optional[_Union[_Unbounded, _Mapping]] = ..., max_score: _Optional[_Union[_SortedSetFetchRequest._ByScore._Score, _Mapping]] = ..., offset: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...
    ASCENDING: _SortedSetFetchRequest.Order
    BY_INDEX_FIELD_NUMBER: _ClassVar[int]
    BY_SCORE_FIELD_NUMBER: _ClassVar[int]
    DESCENDING: _SortedSetFetchRequest.Order
    ORDER_FIELD_NUMBER: _ClassVar[int]
    SET_NAME_FIELD_NUMBER: _ClassVar[int]
    WITH_SCORES_FIELD_NUMBER: _ClassVar[int]
    by_index: _SortedSetFetchRequest._ByIndex
    by_score: _SortedSetFetchRequest._ByScore
    order: _SortedSetFetchRequest.Order
    set_name: bytes
    with_scores: bool
    def __init__(self, set_name: _Optional[bytes] = ..., order: _Optional[_Union[_SortedSetFetchRequest.Order, str]] = ..., with_scores: bool = ..., by_index: _Optional[_Union[_SortedSetFetchRequest._ByIndex, _Mapping]] = ..., by_score: _Optional[_Union[_SortedSetFetchRequest._ByScore, _Mapping]] = ...) -> None: ...

class _SortedSetFetchResponse(_message.Message):
    __slots__ = ["found", "missing"]
    class _Found(_message.Message):
        __slots__ = ["values", "values_with_scores"]
        class _Values(_message.Message):
            __slots__ = ["values"]
            VALUES_FIELD_NUMBER: _ClassVar[int]
            values: _containers.RepeatedScalarFieldContainer[bytes]
            def __init__(self, values: _Optional[_Iterable[bytes]] = ...) -> None: ...
        class _ValuesWithScores(_message.Message):
            __slots__ = ["elements"]
            ELEMENTS_FIELD_NUMBER: _ClassVar[int]
            elements: _containers.RepeatedCompositeFieldContainer[_SortedSetElement]
            def __init__(self, elements: _Optional[_Iterable[_Union[_SortedSetElement, _Mapping]]] = ...) -> None: ...
        VALUES_FIELD_NUMBER: _ClassVar[int]
        VALUES_WITH_SCORES_FIELD_NUMBER: _ClassVar[int]
        values: _SortedSetFetchResponse._Found._Values
        values_with_scores: _SortedSetFetchResponse._Found._ValuesWithScores
        def __init__(self, values_with_scores: _Optional[_Union[_SortedSetFetchResponse._Found._ValuesWithScores, _Mapping]] = ..., values: _Optional[_Union[_SortedSetFetchResponse._Found._Values, _Mapping]] = ...) -> None: ...
    class _Missing(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    FOUND_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELD_NUMBER: _ClassVar[int]
    found: _SortedSetFetchResponse._Found
    missing: _SortedSetFetchResponse._Missing
    def __init__(self, found: _Optional[_Union[_SortedSetFetchResponse._Found, _Mapping]] = ..., missing: _Optional[_Union[_SortedSetFetchResponse._Missing, _Mapping]] = ...) -> None: ...

class _SortedSetGetRankRequest(_message.Message):
    __slots__ = ["order", "set_name", "value"]
    class Order(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ASCENDING: _SortedSetGetRankRequest.Order
    DESCENDING: _SortedSetGetRankRequest.Order
    ORDER_FIELD_NUMBER: _ClassVar[int]
    SET_NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    order: _SortedSetGetRankRequest.Order
    set_name: bytes
    value: bytes
    def __init__(self, set_name: _Optional[bytes] = ..., value: _Optional[bytes] = ..., order: _Optional[_Union[_SortedSetGetRankRequest.Order, str]] = ...) -> None: ...

class _SortedSetGetRankResponse(_message.Message):
    __slots__ = ["element_rank", "missing"]
    class _RankResponsePart(_message.Message):
        __slots__ = ["rank", "result"]
        RANK_FIELD_NUMBER: _ClassVar[int]
        RESULT_FIELD_NUMBER: _ClassVar[int]
        rank: int
        result: ECacheResult
        def __init__(self, result: _Optional[_Union[ECacheResult, str]] = ..., rank: _Optional[int] = ...) -> None: ...
    class _SortedSetMissing(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    ELEMENT_RANK_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELD_NUMBER: _ClassVar[int]
    element_rank: _SortedSetGetRankResponse._RankResponsePart
    missing: _SortedSetGetRankResponse._SortedSetMissing
    def __init__(self, element_rank: _Optional[_Union[_SortedSetGetRankResponse._RankResponsePart, _Mapping]] = ..., missing: _Optional[_Union[_SortedSetGetRankResponse._SortedSetMissing, _Mapping]] = ...) -> None: ...

class _SortedSetGetScoreRequest(_message.Message):
    __slots__ = ["set_name", "values"]
    SET_NAME_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    set_name: bytes
    values: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, set_name: _Optional[bytes] = ..., values: _Optional[_Iterable[bytes]] = ...) -> None: ...

class _SortedSetGetScoreResponse(_message.Message):
    __slots__ = ["found", "missing"]
    class _SortedSetFound(_message.Message):
        __slots__ = ["elements"]
        ELEMENTS_FIELD_NUMBER: _ClassVar[int]
        elements: _containers.RepeatedCompositeFieldContainer[_SortedSetGetScoreResponse._SortedSetGetScoreResponsePart]
        def __init__(self, elements: _Optional[_Iterable[_Union[_SortedSetGetScoreResponse._SortedSetGetScoreResponsePart, _Mapping]]] = ...) -> None: ...
    class _SortedSetGetScoreResponsePart(_message.Message):
        __slots__ = ["result", "score"]
        RESULT_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        result: ECacheResult
        score: float
        def __init__(self, result: _Optional[_Union[ECacheResult, str]] = ..., score: _Optional[float] = ...) -> None: ...
    class _SortedSetMissing(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    FOUND_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELD_NUMBER: _ClassVar[int]
    found: _SortedSetGetScoreResponse._SortedSetFound
    missing: _SortedSetGetScoreResponse._SortedSetMissing
    def __init__(self, found: _Optional[_Union[_SortedSetGetScoreResponse._SortedSetFound, _Mapping]] = ..., missing: _Optional[_Union[_SortedSetGetScoreResponse._SortedSetMissing, _Mapping]] = ...) -> None: ...

class _SortedSetIncrementRequest(_message.Message):
    __slots__ = ["amount", "refresh_ttl", "set_name", "ttl_milliseconds", "value"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TTL_FIELD_NUMBER: _ClassVar[int]
    SET_NAME_FIELD_NUMBER: _ClassVar[int]
    TTL_MILLISECONDS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    amount: float
    refresh_ttl: bool
    set_name: bytes
    ttl_milliseconds: int
    value: bytes
    def __init__(self, set_name: _Optional[bytes] = ..., value: _Optional[bytes] = ..., amount: _Optional[float] = ..., ttl_milliseconds: _Optional[int] = ..., refresh_ttl: bool = ...) -> None: ...

class _SortedSetIncrementResponse(_message.Message):
    __slots__ = ["score"]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float
    def __init__(self, score: _Optional[float] = ...) -> None: ...

class _SortedSetLengthByScoreRequest(_message.Message):
    __slots__ = ["exclusive_max", "exclusive_min", "inclusive_max", "inclusive_min", "set_name", "unbounded_max", "unbounded_min"]
    EXCLUSIVE_MAX_FIELD_NUMBER: _ClassVar[int]
    EXCLUSIVE_MIN_FIELD_NUMBER: _ClassVar[int]
    INCLUSIVE_MAX_FIELD_NUMBER: _ClassVar[int]
    INCLUSIVE_MIN_FIELD_NUMBER: _ClassVar[int]
    SET_NAME_FIELD_NUMBER: _ClassVar[int]
    UNBOUNDED_MAX_FIELD_NUMBER: _ClassVar[int]
    UNBOUNDED_MIN_FIELD_NUMBER: _ClassVar[int]
    exclusive_max: float
    exclusive_min: float
    inclusive_max: float
    inclusive_min: float
    set_name: bytes
    unbounded_max: _Unbounded
    unbounded_min: _Unbounded
    def __init__(self, set_name: _Optional[bytes] = ..., inclusive_min: _Optional[float] = ..., exclusive_min: _Optional[float] = ..., unbounded_min: _Optional[_Union[_Unbounded, _Mapping]] = ..., inclusive_max: _Optional[float] = ..., exclusive_max: _Optional[float] = ..., unbounded_max: _Optional[_Union[_Unbounded, _Mapping]] = ...) -> None: ...

class _SortedSetLengthByScoreResponse(_message.Message):
    __slots__ = ["found", "missing"]
    class _Found(_message.Message):
        __slots__ = ["length"]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        length: int
        def __init__(self, length: _Optional[int] = ...) -> None: ...
    class _Missing(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    FOUND_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELD_NUMBER: _ClassVar[int]
    found: _SortedSetLengthByScoreResponse._Found
    missing: _SortedSetLengthByScoreResponse._Missing
    def __init__(self, found: _Optional[_Union[_SortedSetLengthByScoreResponse._Found, _Mapping]] = ..., missing: _Optional[_Union[_SortedSetLengthByScoreResponse._Missing, _Mapping]] = ...) -> None: ...

class _SortedSetLengthRequest(_message.Message):
    __slots__ = ["set_name"]
    SET_NAME_FIELD_NUMBER: _ClassVar[int]
    set_name: bytes
    def __init__(self, set_name: _Optional[bytes] = ...) -> None: ...

class _SortedSetLengthResponse(_message.Message):
    __slots__ = ["found", "missing"]
    class _Found(_message.Message):
        __slots__ = ["length"]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        length: int
        def __init__(self, length: _Optional[int] = ...) -> None: ...
    class _Missing(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    FOUND_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELD_NUMBER: _ClassVar[int]
    found: _SortedSetLengthResponse._Found
    missing: _SortedSetLengthResponse._Missing
    def __init__(self, found: _Optional[_Union[_SortedSetLengthResponse._Found, _Mapping]] = ..., missing: _Optional[_Union[_SortedSetLengthResponse._Missing, _Mapping]] = ...) -> None: ...

class _SortedSetPutRequest(_message.Message):
    __slots__ = ["elements", "refresh_ttl", "set_name", "ttl_milliseconds"]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TTL_FIELD_NUMBER: _ClassVar[int]
    SET_NAME_FIELD_NUMBER: _ClassVar[int]
    TTL_MILLISECONDS_FIELD_NUMBER: _ClassVar[int]
    elements: _containers.RepeatedCompositeFieldContainer[_SortedSetElement]
    refresh_ttl: bool
    set_name: bytes
    ttl_milliseconds: int
    def __init__(self, set_name: _Optional[bytes] = ..., elements: _Optional[_Iterable[_Union[_SortedSetElement, _Mapping]]] = ..., ttl_milliseconds: _Optional[int] = ..., refresh_ttl: bool = ...) -> None: ...

class _SortedSetPutResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class _SortedSetRemoveRequest(_message.Message):
    __slots__ = ["all", "set_name", "some"]
    class _All(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class _Some(_message.Message):
        __slots__ = ["values"]
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedScalarFieldContainer[bytes]
        def __init__(self, values: _Optional[_Iterable[bytes]] = ...) -> None: ...
    ALL_FIELD_NUMBER: _ClassVar[int]
    SET_NAME_FIELD_NUMBER: _ClassVar[int]
    SOME_FIELD_NUMBER: _ClassVar[int]
    all: _SortedSetRemoveRequest._All
    set_name: bytes
    some: _SortedSetRemoveRequest._Some
    def __init__(self, set_name: _Optional[bytes] = ..., all: _Optional[_Union[_SortedSetRemoveRequest._All, _Mapping]] = ..., some: _Optional[_Union[_SortedSetRemoveRequest._Some, _Mapping]] = ...) -> None: ...

class _SortedSetRemoveResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class _Unbounded(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class _UpdateTtlRequest(_message.Message):
    __slots__ = ["cache_key", "decrease_to_milliseconds", "increase_to_milliseconds", "overwrite_to_milliseconds"]
    CACHE_KEY_FIELD_NUMBER: _ClassVar[int]
    DECREASE_TO_MILLISECONDS_FIELD_NUMBER: _ClassVar[int]
    INCREASE_TO_MILLISECONDS_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_TO_MILLISECONDS_FIELD_NUMBER: _ClassVar[int]
    cache_key: bytes
    decrease_to_milliseconds: int
    increase_to_milliseconds: int
    overwrite_to_milliseconds: int
    def __init__(self, cache_key: _Optional[bytes] = ..., increase_to_milliseconds: _Optional[int] = ..., decrease_to_milliseconds: _Optional[int] = ..., overwrite_to_milliseconds: _Optional[int] = ...) -> None: ...

class _UpdateTtlResponse(_message.Message):
    __slots__ = ["missing", "not_set", "set"]
    class _Missing(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class _NotSet(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class _Set(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    MISSING_FIELD_NUMBER: _ClassVar[int]
    NOT_SET_FIELD_NUMBER: _ClassVar[int]
    SET_FIELD_NUMBER: _ClassVar[int]
    missing: _UpdateTtlResponse._Missing
    not_set: _UpdateTtlResponse._NotSet
    set: _UpdateTtlResponse._Set
    def __init__(self, set: _Optional[_Union[_UpdateTtlResponse._Set, _Mapping]] = ..., not_set: _Optional[_Union[_UpdateTtlResponse._NotSet, _Mapping]] = ..., missing: _Optional[_Union[_UpdateTtlResponse._Missing, _Mapping]] = ...) -> None: ...

class ECacheResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
