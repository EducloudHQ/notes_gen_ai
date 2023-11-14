import permissionmessages_pb2 as _permissionmessages_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class _GenerateDisposableTokenRequest(_message.Message):
    __slots__ = ["auth_token", "expires", "permissions", "token_id"]
    class Expires(_message.Message):
        __slots__ = ["valid_for_seconds"]
        VALID_FOR_SECONDS_FIELD_NUMBER: _ClassVar[int]
        valid_for_seconds: int
        def __init__(self, valid_for_seconds: _Optional[int] = ...) -> None: ...
    AUTH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    auth_token: str
    expires: _GenerateDisposableTokenRequest.Expires
    permissions: _permissionmessages_pb2.Permissions
    token_id: str
    def __init__(self, expires: _Optional[_Union[_GenerateDisposableTokenRequest.Expires, _Mapping]] = ..., auth_token: _Optional[str] = ..., permissions: _Optional[_Union[_permissionmessages_pb2.Permissions, _Mapping]] = ..., token_id: _Optional[str] = ...) -> None: ...

class _GenerateDisposableTokenResponse(_message.Message):
    __slots__ = ["api_key", "endpoint", "valid_until"]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    endpoint: str
    valid_until: int
    def __init__(self, api_key: _Optional[str] = ..., endpoint: _Optional[str] = ..., valid_until: _Optional[int] = ...) -> None: ...
