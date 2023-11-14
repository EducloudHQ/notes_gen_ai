from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class _Cache(_message.Message):
    __slots__ = ["cache_limits", "cache_name", "topic_limits"]
    CACHE_LIMITS_FIELD_NUMBER: _ClassVar[int]
    CACHE_NAME_FIELD_NUMBER: _ClassVar[int]
    TOPIC_LIMITS_FIELD_NUMBER: _ClassVar[int]
    cache_limits: _CacheLimits
    cache_name: str
    topic_limits: _TopicLimits
    def __init__(self, cache_name: _Optional[str] = ..., cache_limits: _Optional[_Union[_CacheLimits, _Mapping]] = ..., topic_limits: _Optional[_Union[_TopicLimits, _Mapping]] = ...) -> None: ...

class _CacheLimits(_message.Message):
    __slots__ = ["max_item_size_kb", "max_throughput_kbps", "max_traffic_rate", "max_ttl_seconds"]
    MAX_ITEM_SIZE_KB_FIELD_NUMBER: _ClassVar[int]
    MAX_THROUGHPUT_KBPS_FIELD_NUMBER: _ClassVar[int]
    MAX_TRAFFIC_RATE_FIELD_NUMBER: _ClassVar[int]
    MAX_TTL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    max_item_size_kb: int
    max_throughput_kbps: int
    max_traffic_rate: int
    max_ttl_seconds: int
    def __init__(self, max_traffic_rate: _Optional[int] = ..., max_throughput_kbps: _Optional[int] = ..., max_item_size_kb: _Optional[int] = ..., max_ttl_seconds: _Optional[int] = ...) -> None: ...

class _CreateCacheRequest(_message.Message):
    __slots__ = ["cache_name"]
    CACHE_NAME_FIELD_NUMBER: _ClassVar[int]
    cache_name: str
    def __init__(self, cache_name: _Optional[str] = ...) -> None: ...

class _CreateCacheResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class _CreateIndexRequest(_message.Message):
    __slots__ = ["cosine_similarity", "euclidean_similarity", "index_name", "inner_product", "num_dimensions"]
    class _CosineSimilarity(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class _EuclideanSimilarity(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class _InnerProduct(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    COSINE_SIMILARITY_FIELD_NUMBER: _ClassVar[int]
    EUCLIDEAN_SIMILARITY_FIELD_NUMBER: _ClassVar[int]
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    INNER_PRODUCT_FIELD_NUMBER: _ClassVar[int]
    NUM_DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    cosine_similarity: _CreateIndexRequest._CosineSimilarity
    euclidean_similarity: _CreateIndexRequest._EuclideanSimilarity
    index_name: str
    inner_product: _CreateIndexRequest._InnerProduct
    num_dimensions: int
    def __init__(self, index_name: _Optional[str] = ..., num_dimensions: _Optional[int] = ..., euclidean_similarity: _Optional[_Union[_CreateIndexRequest._EuclideanSimilarity, _Mapping]] = ..., inner_product: _Optional[_Union[_CreateIndexRequest._InnerProduct, _Mapping]] = ..., cosine_similarity: _Optional[_Union[_CreateIndexRequest._CosineSimilarity, _Mapping]] = ...) -> None: ...

class _CreateIndexResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class _CreateSigningKeyRequest(_message.Message):
    __slots__ = ["ttl_minutes"]
    TTL_MINUTES_FIELD_NUMBER: _ClassVar[int]
    ttl_minutes: int
    def __init__(self, ttl_minutes: _Optional[int] = ...) -> None: ...

class _CreateSigningKeyResponse(_message.Message):
    __slots__ = ["expires_at", "key"]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    expires_at: int
    key: str
    def __init__(self, key: _Optional[str] = ..., expires_at: _Optional[int] = ...) -> None: ...

class _DeleteCacheRequest(_message.Message):
    __slots__ = ["cache_name"]
    CACHE_NAME_FIELD_NUMBER: _ClassVar[int]
    cache_name: str
    def __init__(self, cache_name: _Optional[str] = ...) -> None: ...

class _DeleteCacheResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class _DeleteIndexRequest(_message.Message):
    __slots__ = ["index_name"]
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    index_name: str
    def __init__(self, index_name: _Optional[str] = ...) -> None: ...

class _DeleteIndexResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class _FlushCacheRequest(_message.Message):
    __slots__ = ["cache_name"]
    CACHE_NAME_FIELD_NUMBER: _ClassVar[int]
    cache_name: str
    def __init__(self, cache_name: _Optional[str] = ...) -> None: ...

class _FlushCacheResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class _ListCachesRequest(_message.Message):
    __slots__ = ["next_token"]
    NEXT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    next_token: str
    def __init__(self, next_token: _Optional[str] = ...) -> None: ...

class _ListCachesResponse(_message.Message):
    __slots__ = ["cache", "next_token"]
    CACHE_FIELD_NUMBER: _ClassVar[int]
    NEXT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    cache: _containers.RepeatedCompositeFieldContainer[_Cache]
    next_token: str
    def __init__(self, cache: _Optional[_Iterable[_Union[_Cache, _Mapping]]] = ..., next_token: _Optional[str] = ...) -> None: ...

class _ListIndexesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class _ListIndexesResponse(_message.Message):
    __slots__ = ["index_names"]
    INDEX_NAMES_FIELD_NUMBER: _ClassVar[int]
    index_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, index_names: _Optional[_Iterable[str]] = ...) -> None: ...

class _ListSigningKeysRequest(_message.Message):
    __slots__ = ["next_token"]
    NEXT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    next_token: str
    def __init__(self, next_token: _Optional[str] = ...) -> None: ...

class _ListSigningKeysResponse(_message.Message):
    __slots__ = ["next_token", "signing_key"]
    NEXT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SIGNING_KEY_FIELD_NUMBER: _ClassVar[int]
    next_token: str
    signing_key: _containers.RepeatedCompositeFieldContainer[_SigningKey]
    def __init__(self, signing_key: _Optional[_Iterable[_Union[_SigningKey, _Mapping]]] = ..., next_token: _Optional[str] = ...) -> None: ...

class _RevokeSigningKeyRequest(_message.Message):
    __slots__ = ["key_id"]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    key_id: str
    def __init__(self, key_id: _Optional[str] = ...) -> None: ...

class _RevokeSigningKeyResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class _SigningKey(_message.Message):
    __slots__ = ["expires_at", "key_id"]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    expires_at: int
    key_id: str
    def __init__(self, key_id: _Optional[str] = ..., expires_at: _Optional[int] = ...) -> None: ...

class _TopicLimits(_message.Message):
    __slots__ = ["max_publish_message_size_kb", "max_publish_rate", "max_subscription_count"]
    MAX_PUBLISH_MESSAGE_SIZE_KB_FIELD_NUMBER: _ClassVar[int]
    MAX_PUBLISH_RATE_FIELD_NUMBER: _ClassVar[int]
    MAX_SUBSCRIPTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    max_publish_message_size_kb: int
    max_publish_rate: int
    max_subscription_count: int
    def __init__(self, max_publish_rate: _Optional[int] = ..., max_subscription_count: _Optional[int] = ..., max_publish_message_size_kb: _Optional[int] = ...) -> None: ...
