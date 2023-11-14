import google.protobuf as protobuf

try:
    protobuf_version = protobuf.__version__.split(".")
    major = int(protobuf_version[0])
    minor = int(protobuf_version[1])
except ValueError:
    raise ValueError("Could not parse protobuf version: {}".format(protobuf.__version__))

# Import the correct version of the generated code.
# To accomodate the dynamic imports, we must now write code like:
#       from momento_wire_types import cacheclient_pb2 as cache_pb
#       request = cache_pb.GetRequest()
# instead of:
#       from momento_wire_types.cacheclient_pb2 import GetRequest
#       request = GetRequest()
# This because the multi-level from will not work with the dynamic imports.
if major >= 4 or (major == 3 and minor >= 20):
    from .v4 import auth_pb2 as auth_pb2
    from .v4 import auth_pb2_grpc as auth_pb2_grpc
    from .v4 import cacheclient_pb2 as cacheclient_pb2
    from .v4 import cacheclient_pb2_grpc as cacheclient_pb2_grpc
    from .v4 import cachepubsub_pb2 as cachepubsub_pb2
    from .v4 import cachepubsub_pb2_grpc as cachepubsub_pb2_grpc
    from .v4 import controlclient_pb2 as controlclient_pb2
    from .v4 import controlclient_pb2_grpc as controlclient_pb2_grpc
    from .v4 import extensions_pb2 as extensions_pb2
    from .v4 import extensions_pb2_grpc as extensions_pb2_grpc
    from .v4 import permissionmessages_pb2 as permissionmessages_pb2
    from .v4 import permissionmessages_pb2_grpc as permissionmessages_pb2_grpc
    from .v4 import token_pb2 as token_pb2
    from .v4 import token_pb2_grpc as token_pb2_grpc
    from .v4 import vectorindex_pb2 as vectorindex_pb2
    from .v4 import vectorindex_pb2_grpc as vectorindex_pb2_grpc

else:
    from .v319 import auth_pb2 as auth_pb2
    from .v319 import auth_pb2_grpc as auth_pb2_grpc
    from .v319 import cacheclient_pb2 as cacheclient_pb2
    from .v319 import cacheclient_pb2_grpc as cacheclient_pb2_grpc
    from .v319 import cachepubsub_pb2 as cachepubsub_pb2
    from .v319 import cachepubsub_pb2_grpc as cachepubsub_pb2_grpc
    from .v319 import controlclient_pb2 as controlclient_pb2
    from .v319 import controlclient_pb2_grpc as controlclient_pb2_grpc
    from .v319 import extensions_pb2 as extensions_pb2
    from .v319 import extensions_pb2_grpc as extensions_pb2_grpc
    from .v319 import permissionmessages_pb2 as permissionmessages_pb2
    from .v319 import permissionmessages_pb2_grpc as permissionmessages_pb2_grpc
    from .v319 import token_pb2 as token_pb2
    from .v319 import token_pb2_grpc as token_pb2_grpc
    from .v319 import vectorindex_pb2 as vectorindex_pb2
    from .v319 import vectorindex_pb2_grpc as vectorindex_pb2_grpc


__all__ = ["auth_pb2", "auth_pb2_grpc", "cacheclient_pb2", "cacheclient_pb2_grpc", "cachepubsub_pb2", "cachepubsub_pb2_grpc", "controlclient_pb2", "controlclient_pb2_grpc", "extensions_pb2", "extensions_pb2_grpc", "permissionmessages_pb2", "permissionmessages_pb2_grpc", "token_pb2", "token_pb2_grpc", "vectorindex_pb2", "vectorindex_pb2_grpc"]