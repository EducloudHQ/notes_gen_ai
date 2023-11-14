# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import vectorindex_pb2 as vectorindex__pb2


class VectorIndexStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UpsertItemBatch = channel.unary_unary(
                '/vectorindex.VectorIndex/UpsertItemBatch',
                request_serializer=vectorindex__pb2._UpsertItemBatchRequest.SerializeToString,
                response_deserializer=vectorindex__pb2._UpsertItemBatchResponse.FromString,
                )
        self.DeleteItemBatch = channel.unary_unary(
                '/vectorindex.VectorIndex/DeleteItemBatch',
                request_serializer=vectorindex__pb2._DeleteItemBatchRequest.SerializeToString,
                response_deserializer=vectorindex__pb2._DeleteItemBatchResponse.FromString,
                )
        self.Search = channel.unary_unary(
                '/vectorindex.VectorIndex/Search',
                request_serializer=vectorindex__pb2._SearchRequest.SerializeToString,
                response_deserializer=vectorindex__pb2._SearchResponse.FromString,
                )


class VectorIndexServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UpsertItemBatch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteItemBatch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Search(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VectorIndexServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UpsertItemBatch': grpc.unary_unary_rpc_method_handler(
                    servicer.UpsertItemBatch,
                    request_deserializer=vectorindex__pb2._UpsertItemBatchRequest.FromString,
                    response_serializer=vectorindex__pb2._UpsertItemBatchResponse.SerializeToString,
            ),
            'DeleteItemBatch': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteItemBatch,
                    request_deserializer=vectorindex__pb2._DeleteItemBatchRequest.FromString,
                    response_serializer=vectorindex__pb2._DeleteItemBatchResponse.SerializeToString,
            ),
            'Search': grpc.unary_unary_rpc_method_handler(
                    servicer.Search,
                    request_deserializer=vectorindex__pb2._SearchRequest.FromString,
                    response_serializer=vectorindex__pb2._SearchResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'vectorindex.VectorIndex', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class VectorIndex(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UpsertItemBatch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vectorindex.VectorIndex/UpsertItemBatch',
            vectorindex__pb2._UpsertItemBatchRequest.SerializeToString,
            vectorindex__pb2._UpsertItemBatchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteItemBatch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vectorindex.VectorIndex/DeleteItemBatch',
            vectorindex__pb2._DeleteItemBatchRequest.SerializeToString,
            vectorindex__pb2._DeleteItemBatchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Search(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vectorindex.VectorIndex/Search',
            vectorindex__pb2._SearchRequest.SerializeToString,
            vectorindex__pb2._SearchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
