from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

CachePermitNone: CacheRole
CacheReadOnly: CacheRole
CacheReadWrite: CacheRole
CacheWriteOnly: CacheRole
DESCRIPTOR: _descriptor.FileDescriptor
SuperUser: SuperUserPermissions
TopicPermitNone: TopicRole
TopicReadOnly: TopicRole
TopicReadWrite: TopicRole
TopicWriteOnly: TopicRole

class ExplicitPermissions(_message.Message):
    __slots__ = ["permissions"]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedCompositeFieldContainer[PermissionsType]
    def __init__(self, permissions: _Optional[_Iterable[_Union[PermissionsType, _Mapping]]] = ...) -> None: ...

class Permissions(_message.Message):
    __slots__ = ["explicit", "super_user"]
    EXPLICIT_FIELD_NUMBER: _ClassVar[int]
    SUPER_USER_FIELD_NUMBER: _ClassVar[int]
    explicit: ExplicitPermissions
    super_user: SuperUserPermissions
    def __init__(self, super_user: _Optional[_Union[SuperUserPermissions, str]] = ..., explicit: _Optional[_Union[ExplicitPermissions, _Mapping]] = ...) -> None: ...

class PermissionsType(_message.Message):
    __slots__ = ["cache_permissions", "topic_permissions"]
    class All(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class CacheItemSelector(_message.Message):
        __slots__ = ["key", "key_prefix"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        KEY_PREFIX_FIELD_NUMBER: _ClassVar[int]
        key: bytes
        key_prefix: bytes
        def __init__(self, key: _Optional[bytes] = ..., key_prefix: _Optional[bytes] = ...) -> None: ...
    class CachePermissions(_message.Message):
        __slots__ = ["all_caches", "all_items", "cache_selector", "item_selector", "role"]
        ALL_CACHES_FIELD_NUMBER: _ClassVar[int]
        ALL_ITEMS_FIELD_NUMBER: _ClassVar[int]
        CACHE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
        ITEM_SELECTOR_FIELD_NUMBER: _ClassVar[int]
        ROLE_FIELD_NUMBER: _ClassVar[int]
        all_caches: PermissionsType.All
        all_items: PermissionsType.All
        cache_selector: PermissionsType.CacheSelector
        item_selector: PermissionsType.CacheItemSelector
        role: CacheRole
        def __init__(self, role: _Optional[_Union[CacheRole, str]] = ..., all_caches: _Optional[_Union[PermissionsType.All, _Mapping]] = ..., cache_selector: _Optional[_Union[PermissionsType.CacheSelector, _Mapping]] = ..., all_items: _Optional[_Union[PermissionsType.All, _Mapping]] = ..., item_selector: _Optional[_Union[PermissionsType.CacheItemSelector, _Mapping]] = ...) -> None: ...
    class CacheSelector(_message.Message):
        __slots__ = ["cache_name"]
        CACHE_NAME_FIELD_NUMBER: _ClassVar[int]
        cache_name: str
        def __init__(self, cache_name: _Optional[str] = ...) -> None: ...
    class TopicPermissions(_message.Message):
        __slots__ = ["all_caches", "all_topics", "cache_selector", "role", "topic_selector"]
        ALL_CACHES_FIELD_NUMBER: _ClassVar[int]
        ALL_TOPICS_FIELD_NUMBER: _ClassVar[int]
        CACHE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
        ROLE_FIELD_NUMBER: _ClassVar[int]
        TOPIC_SELECTOR_FIELD_NUMBER: _ClassVar[int]
        all_caches: PermissionsType.All
        all_topics: PermissionsType.All
        cache_selector: PermissionsType.CacheSelector
        role: TopicRole
        topic_selector: PermissionsType.TopicSelector
        def __init__(self, role: _Optional[_Union[TopicRole, str]] = ..., all_caches: _Optional[_Union[PermissionsType.All, _Mapping]] = ..., cache_selector: _Optional[_Union[PermissionsType.CacheSelector, _Mapping]] = ..., all_topics: _Optional[_Union[PermissionsType.All, _Mapping]] = ..., topic_selector: _Optional[_Union[PermissionsType.TopicSelector, _Mapping]] = ...) -> None: ...
    class TopicSelector(_message.Message):
        __slots__ = ["topic_name", "topic_name_prefix"]
        TOPIC_NAME_FIELD_NUMBER: _ClassVar[int]
        TOPIC_NAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
        topic_name: str
        topic_name_prefix: str
        def __init__(self, topic_name: _Optional[str] = ..., topic_name_prefix: _Optional[str] = ...) -> None: ...
    CACHE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    TOPIC_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    cache_permissions: PermissionsType.CachePermissions
    topic_permissions: PermissionsType.TopicPermissions
    def __init__(self, cache_permissions: _Optional[_Union[PermissionsType.CachePermissions, _Mapping]] = ..., topic_permissions: _Optional[_Union[PermissionsType.TopicPermissions, _Mapping]] = ...) -> None: ...

class CacheRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class TopicRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class SuperUserPermissions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
