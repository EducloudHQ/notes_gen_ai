# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vectorindex.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11vectorindex.proto\x12\x0bvectorindex\"c\n\x05_Item\x12\n\n\x02id\x18\x01 \x01(\t\x12$\n\x06vector\x18\x02 \x01(\x0b\x32\x14.vectorindex._Vector\x12(\n\x08metadata\x18\x03 \x03(\x0b\x32\x16.vectorindex._Metadata\"P\n\x17_UpsertItemBatchRequest\x12\x12\n\nindex_name\x18\x01 \x01(\t\x12!\n\x05items\x18\x02 \x03(\x0b\x32\x12.vectorindex._Item\"1\n\x18_UpsertItemBatchResponse\x12\x15\n\rerror_indices\x18\x01 \x03(\r\":\n\x17_DeleteItemBatchRequest\x12\x12\n\nindex_name\x18\x01 \x01(\t\x12\x0b\n\x03ids\x18\x02 \x03(\t\"\x1a\n\x18_DeleteItemBatchResponse\"\x1b\n\x07_Vector\x12\x10\n\x08\x65lements\x18\x01 \x03(\x02\"\xef\x01\n\t_Metadata\x12\r\n\x05\x66ield\x18\x01 \x01(\t\x12\x16\n\x0cstring_value\x18\x02 \x01(\tH\x00\x12\x17\n\rinteger_value\x18\x03 \x01(\x03H\x00\x12\x16\n\x0c\x64ouble_value\x18\x04 \x01(\x01H\x00\x12\x17\n\rboolean_value\x18\x05 \x01(\x08H\x00\x12\x46\n\x15list_of_strings_value\x18\x06 \x01(\x0b\x32%.vectorindex._Metadata._ListOfStringsH\x00\x1a \n\x0e_ListOfStrings\x12\x0e\n\x06values\x18\x01 \x03(\tB\x07\n\x05value\"\x9f\x01\n\x10_MetadataRequest\x12\x32\n\x04some\x18\x02 \x01(\x0b\x32\".vectorindex._MetadataRequest.SomeH\x00\x12\x30\n\x03\x61ll\x18\x03 \x01(\x0b\x32!.vectorindex._MetadataRequest.AllH\x00\x1a\x16\n\x04Some\x12\x0e\n\x06\x66ields\x18\x01 \x03(\t\x1a\x05\n\x03\x41llB\x06\n\x04kind\"\x97\x01\n\x0e_SearchRequest\x12\x12\n\nindex_name\x18\x01 \x01(\t\x12\r\n\x05top_k\x18\x02 \x01(\r\x12*\n\x0cquery_vector\x18\x03 \x01(\x0b\x32\x14.vectorindex._Vector\x12\x36\n\x0fmetadata_fields\x18\x04 \x01(\x0b\x32\x1d.vectorindex._MetadataRequest\"T\n\n_SearchHit\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08\x64istance\x18\x02 \x01(\x02\x12(\n\x08metadata\x18\x03 \x03(\x0b\x32\x16.vectorindex._Metadata\"8\n\x0f_SearchResponse\x12%\n\x04hits\x18\x01 \x03(\x0b\x32\x17.vectorindex._SearchHit2\x98\x02\n\x0bVectorIndex\x12`\n\x0fUpsertItemBatch\x12$.vectorindex._UpsertItemBatchRequest\x1a%.vectorindex._UpsertItemBatchResponse\"\x00\x12`\n\x0f\x44\x65leteItemBatch\x12$.vectorindex._DeleteItemBatchRequest\x1a%.vectorindex._DeleteItemBatchResponse\"\x00\x12\x45\n\x06Search\x12\x1b.vectorindex._SearchRequest\x1a\x1c.vectorindex._SearchResponse\"\x00\x62\x06proto3')



__ITEM = DESCRIPTOR.message_types_by_name['_Item']
__UPSERTITEMBATCHREQUEST = DESCRIPTOR.message_types_by_name['_UpsertItemBatchRequest']
__UPSERTITEMBATCHRESPONSE = DESCRIPTOR.message_types_by_name['_UpsertItemBatchResponse']
__DELETEITEMBATCHREQUEST = DESCRIPTOR.message_types_by_name['_DeleteItemBatchRequest']
__DELETEITEMBATCHRESPONSE = DESCRIPTOR.message_types_by_name['_DeleteItemBatchResponse']
__VECTOR = DESCRIPTOR.message_types_by_name['_Vector']
__METADATA = DESCRIPTOR.message_types_by_name['_Metadata']
__METADATA__LISTOFSTRINGS = __METADATA.nested_types_by_name['_ListOfStrings']
__METADATAREQUEST = DESCRIPTOR.message_types_by_name['_MetadataRequest']
__METADATAREQUEST_SOME = __METADATAREQUEST.nested_types_by_name['Some']
__METADATAREQUEST_ALL = __METADATAREQUEST.nested_types_by_name['All']
__SEARCHREQUEST = DESCRIPTOR.message_types_by_name['_SearchRequest']
__SEARCHHIT = DESCRIPTOR.message_types_by_name['_SearchHit']
__SEARCHRESPONSE = DESCRIPTOR.message_types_by_name['_SearchResponse']
_Item = _reflection.GeneratedProtocolMessageType('_Item', (_message.Message,), {
  'DESCRIPTOR' : __ITEM,
  '__module__' : 'vectorindex_pb2'
  # @@protoc_insertion_point(class_scope:vectorindex._Item)
  })
_sym_db.RegisterMessage(_Item)

_UpsertItemBatchRequest = _reflection.GeneratedProtocolMessageType('_UpsertItemBatchRequest', (_message.Message,), {
  'DESCRIPTOR' : __UPSERTITEMBATCHREQUEST,
  '__module__' : 'vectorindex_pb2'
  # @@protoc_insertion_point(class_scope:vectorindex._UpsertItemBatchRequest)
  })
_sym_db.RegisterMessage(_UpsertItemBatchRequest)

_UpsertItemBatchResponse = _reflection.GeneratedProtocolMessageType('_UpsertItemBatchResponse', (_message.Message,), {
  'DESCRIPTOR' : __UPSERTITEMBATCHRESPONSE,
  '__module__' : 'vectorindex_pb2'
  # @@protoc_insertion_point(class_scope:vectorindex._UpsertItemBatchResponse)
  })
_sym_db.RegisterMessage(_UpsertItemBatchResponse)

_DeleteItemBatchRequest = _reflection.GeneratedProtocolMessageType('_DeleteItemBatchRequest', (_message.Message,), {
  'DESCRIPTOR' : __DELETEITEMBATCHREQUEST,
  '__module__' : 'vectorindex_pb2'
  # @@protoc_insertion_point(class_scope:vectorindex._DeleteItemBatchRequest)
  })
_sym_db.RegisterMessage(_DeleteItemBatchRequest)

_DeleteItemBatchResponse = _reflection.GeneratedProtocolMessageType('_DeleteItemBatchResponse', (_message.Message,), {
  'DESCRIPTOR' : __DELETEITEMBATCHRESPONSE,
  '__module__' : 'vectorindex_pb2'
  # @@protoc_insertion_point(class_scope:vectorindex._DeleteItemBatchResponse)
  })
_sym_db.RegisterMessage(_DeleteItemBatchResponse)

_Vector = _reflection.GeneratedProtocolMessageType('_Vector', (_message.Message,), {
  'DESCRIPTOR' : __VECTOR,
  '__module__' : 'vectorindex_pb2'
  # @@protoc_insertion_point(class_scope:vectorindex._Vector)
  })
_sym_db.RegisterMessage(_Vector)

_Metadata = _reflection.GeneratedProtocolMessageType('_Metadata', (_message.Message,), {

  '_ListOfStrings' : _reflection.GeneratedProtocolMessageType('_ListOfStrings', (_message.Message,), {
    'DESCRIPTOR' : __METADATA__LISTOFSTRINGS,
    '__module__' : 'vectorindex_pb2'
    # @@protoc_insertion_point(class_scope:vectorindex._Metadata._ListOfStrings)
    })
  ,
  'DESCRIPTOR' : __METADATA,
  '__module__' : 'vectorindex_pb2'
  # @@protoc_insertion_point(class_scope:vectorindex._Metadata)
  })
_sym_db.RegisterMessage(_Metadata)
_sym_db.RegisterMessage(_Metadata._ListOfStrings)

_MetadataRequest = _reflection.GeneratedProtocolMessageType('_MetadataRequest', (_message.Message,), {

  'Some' : _reflection.GeneratedProtocolMessageType('Some', (_message.Message,), {
    'DESCRIPTOR' : __METADATAREQUEST_SOME,
    '__module__' : 'vectorindex_pb2'
    # @@protoc_insertion_point(class_scope:vectorindex._MetadataRequest.Some)
    })
  ,

  'All' : _reflection.GeneratedProtocolMessageType('All', (_message.Message,), {
    'DESCRIPTOR' : __METADATAREQUEST_ALL,
    '__module__' : 'vectorindex_pb2'
    # @@protoc_insertion_point(class_scope:vectorindex._MetadataRequest.All)
    })
  ,
  'DESCRIPTOR' : __METADATAREQUEST,
  '__module__' : 'vectorindex_pb2'
  # @@protoc_insertion_point(class_scope:vectorindex._MetadataRequest)
  })
_sym_db.RegisterMessage(_MetadataRequest)
_sym_db.RegisterMessage(_MetadataRequest.Some)
_sym_db.RegisterMessage(_MetadataRequest.All)

_SearchRequest = _reflection.GeneratedProtocolMessageType('_SearchRequest', (_message.Message,), {
  'DESCRIPTOR' : __SEARCHREQUEST,
  '__module__' : 'vectorindex_pb2'
  # @@protoc_insertion_point(class_scope:vectorindex._SearchRequest)
  })
_sym_db.RegisterMessage(_SearchRequest)

_SearchHit = _reflection.GeneratedProtocolMessageType('_SearchHit', (_message.Message,), {
  'DESCRIPTOR' : __SEARCHHIT,
  '__module__' : 'vectorindex_pb2'
  # @@protoc_insertion_point(class_scope:vectorindex._SearchHit)
  })
_sym_db.RegisterMessage(_SearchHit)

_SearchResponse = _reflection.GeneratedProtocolMessageType('_SearchResponse', (_message.Message,), {
  'DESCRIPTOR' : __SEARCHRESPONSE,
  '__module__' : 'vectorindex_pb2'
  # @@protoc_insertion_point(class_scope:vectorindex._SearchResponse)
  })
_sym_db.RegisterMessage(_SearchResponse)

_VECTORINDEX = DESCRIPTOR.services_by_name['VectorIndex']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  __ITEM._serialized_start=34
  __ITEM._serialized_end=133
  __UPSERTITEMBATCHREQUEST._serialized_start=135
  __UPSERTITEMBATCHREQUEST._serialized_end=215
  __UPSERTITEMBATCHRESPONSE._serialized_start=217
  __UPSERTITEMBATCHRESPONSE._serialized_end=266
  __DELETEITEMBATCHREQUEST._serialized_start=268
  __DELETEITEMBATCHREQUEST._serialized_end=326
  __DELETEITEMBATCHRESPONSE._serialized_start=328
  __DELETEITEMBATCHRESPONSE._serialized_end=354
  __VECTOR._serialized_start=356
  __VECTOR._serialized_end=383
  __METADATA._serialized_start=386
  __METADATA._serialized_end=625
  __METADATA__LISTOFSTRINGS._serialized_start=584
  __METADATA__LISTOFSTRINGS._serialized_end=616
  __METADATAREQUEST._serialized_start=628
  __METADATAREQUEST._serialized_end=787
  __METADATAREQUEST_SOME._serialized_start=750
  __METADATAREQUEST_SOME._serialized_end=772
  __METADATAREQUEST_ALL._serialized_start=774
  __METADATAREQUEST_ALL._serialized_end=779
  __SEARCHREQUEST._serialized_start=790
  __SEARCHREQUEST._serialized_end=941
  __SEARCHHIT._serialized_start=943
  __SEARCHHIT._serialized_end=1027
  __SEARCHRESPONSE._serialized_start=1029
  __SEARCHRESPONSE._serialized_end=1085
  _VECTORINDEX._serialized_start=1088
  _VECTORINDEX._serialized_end=1368
# @@protoc_insertion_point(module_scope)
