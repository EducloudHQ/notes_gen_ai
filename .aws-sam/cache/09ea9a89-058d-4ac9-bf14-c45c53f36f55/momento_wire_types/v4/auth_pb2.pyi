import permissionmessages_pb2 as _permissionmessages_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class _GenerateApiTokenRequest(_message.Message):
    __slots__ = ["auth_token", "expires", "never", "permissions", "token_id"]
    class Expires(_message.Message):
        __slots__ = ["valid_for_seconds"]
        VALID_FOR_SECONDS_FIELD_NUMBER: _ClassVar[int]
        valid_for_seconds: int
        def __init__(self, valid_for_seconds: _Optional[int] = ...) -> None: ...
    class Never(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    AUTH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_FIELD_NUMBER: _ClassVar[int]
    NEVER_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    auth_token: str
    expires: _GenerateApiTokenRequest.Expires
    never: _GenerateApiTokenRequest.Never
    permissions: _permissionmessages_pb2.Permissions
    token_id: str
    def __init__(self, never: _Optional[_Union[_GenerateApiTokenRequest.Never, _Mapping]] = ..., expires: _Optional[_Union[_GenerateApiTokenRequest.Expires, _Mapping]] = ..., auth_token: _Optional[str] = ..., permissions: _Optional[_Union[_permissionmessages_pb2.Permissions, _Mapping]] = ..., token_id: _Optional[str] = ...) -> None: ...

class _GenerateApiTokenResponse(_message.Message):
    __slots__ = ["api_key", "endpoint", "refresh_token", "valid_until"]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    endpoint: str
    refresh_token: str
    valid_until: int
    def __init__(self, api_key: _Optional[str] = ..., refresh_token: _Optional[str] = ..., endpoint: _Optional[str] = ..., valid_until: _Optional[int] = ...) -> None: ...

class _LoginRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class _LoginResponse(_message.Message):
    __slots__ = ["direct_browser", "error", "logged_in", "message"]
    class DirectBrowser(_message.Message):
        __slots__ = ["url"]
        URL_FIELD_NUMBER: _ClassVar[int]
        url: str
        def __init__(self, url: _Optional[str] = ...) -> None: ...
    class Error(_message.Message):
        __slots__ = ["description"]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        description: str
        def __init__(self, description: _Optional[str] = ...) -> None: ...
    class LoggedIn(_message.Message):
        __slots__ = ["session_token", "valid_for_seconds"]
        SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
        VALID_FOR_SECONDS_FIELD_NUMBER: _ClassVar[int]
        session_token: str
        valid_for_seconds: int
        def __init__(self, session_token: _Optional[str] = ..., valid_for_seconds: _Optional[int] = ...) -> None: ...
    class Message(_message.Message):
        __slots__ = ["text"]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        text: str
        def __init__(self, text: _Optional[str] = ...) -> None: ...
    DIRECT_BROWSER_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LOGGED_IN_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    direct_browser: _LoginResponse.DirectBrowser
    error: _LoginResponse.Error
    logged_in: _LoginResponse.LoggedIn
    message: _LoginResponse.Message
    def __init__(self, direct_browser: _Optional[_Union[_LoginResponse.DirectBrowser, _Mapping]] = ..., logged_in: _Optional[_Union[_LoginResponse.LoggedIn, _Mapping]] = ..., message: _Optional[_Union[_LoginResponse.Message, _Mapping]] = ..., error: _Optional[_Union[_LoginResponse.Error, _Mapping]] = ...) -> None: ...

class _RefreshApiTokenRequest(_message.Message):
    __slots__ = ["api_key", "refresh_token"]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    refresh_token: str
    def __init__(self, api_key: _Optional[str] = ..., refresh_token: _Optional[str] = ...) -> None: ...

class _RefreshApiTokenResponse(_message.Message):
    __slots__ = ["api_key", "endpoint", "refresh_token", "valid_until"]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    endpoint: str
    refresh_token: str
    valid_until: int
    def __init__(self, api_key: _Optional[str] = ..., refresh_token: _Optional[str] = ..., endpoint: _Optional[str] = ..., valid_until: _Optional[int] = ...) -> None: ...
