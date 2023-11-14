# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cachepubsub.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import extensions_pb2 as extensions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x63\x61\x63hepubsub.proto\x12\x13\x63\x61\x63he_client.pubsub\x1a\x10\x65xtensions.proto\"\x08\n\x06_Empty\"k\n\x0f_PublishRequest\x12\x12\n\ncache_name\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x12/\n\x05value\x18\x03 \x01(\x0b\x32 .cache_client.pubsub._TopicValue:\x04\x80\xb5\x18\x00\"h\n\x14_SubscriptionRequest\x12\x12\n\ncache_name\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x12\'\n\x1fresume_at_topic_sequence_number\x18\x03 \x01(\x04:\x04\x80\xb5\x18\x01\"\xc0\x01\n\x11_SubscriptionItem\x12/\n\x04item\x18\x01 \x01(\x0b\x32\x1f.cache_client.pubsub._TopicItemH\x00\x12<\n\rdiscontinuity\x18\x02 \x01(\x0b\x32#.cache_client.pubsub._DiscontinuityH\x00\x12\x34\n\theartbeat\x18\x03 \x01(\x0b\x32\x1f.cache_client.pubsub._HeartbeatH\x00\x42\x06\n\x04kind\"\\\n\n_TopicItem\x12\x1d\n\x15topic_sequence_number\x18\x01 \x01(\x04\x12/\n\x05value\x18\x02 \x01(\x0b\x32 .cache_client.pubsub._TopicValue\"7\n\x0b_TopicValue\x12\x0e\n\x04text\x18\x01 \x01(\tH\x00\x12\x10\n\x06\x62inary\x18\x02 \x01(\x0cH\x00\x42\x06\n\x04kind\"I\n\x0e_Discontinuity\x12\x1b\n\x13last_topic_sequence\x18\x01 \x01(\x04\x12\x1a\n\x12new_topic_sequence\x18\x02 \x01(\x04\"\x0c\n\n_Heartbeat2\xb8\x01\n\x06Pubsub\x12L\n\x07Publish\x12$.cache_client.pubsub._PublishRequest\x1a\x1b.cache_client.pubsub._Empty\x12`\n\tSubscribe\x12).cache_client.pubsub._SubscriptionRequest\x1a&.cache_client.pubsub._SubscriptionItem0\x01\x42r\n\x18grpc.cache_client.pubsubP\x01Z0github.com/momentohq/client-sdk-go;client_sdk_go\xaa\x02!Momento.Protos.CacheClient.Pubsubb\x06proto3')



__EMPTY = DESCRIPTOR.message_types_by_name['_Empty']
__PUBLISHREQUEST = DESCRIPTOR.message_types_by_name['_PublishRequest']
__SUBSCRIPTIONREQUEST = DESCRIPTOR.message_types_by_name['_SubscriptionRequest']
__SUBSCRIPTIONITEM = DESCRIPTOR.message_types_by_name['_SubscriptionItem']
__TOPICITEM = DESCRIPTOR.message_types_by_name['_TopicItem']
__TOPICVALUE = DESCRIPTOR.message_types_by_name['_TopicValue']
__DISCONTINUITY = DESCRIPTOR.message_types_by_name['_Discontinuity']
__HEARTBEAT = DESCRIPTOR.message_types_by_name['_Heartbeat']
_Empty = _reflection.GeneratedProtocolMessageType('_Empty', (_message.Message,), {
  'DESCRIPTOR' : __EMPTY,
  '__module__' : 'cachepubsub_pb2'
  # @@protoc_insertion_point(class_scope:cache_client.pubsub._Empty)
  })
_sym_db.RegisterMessage(_Empty)

_PublishRequest = _reflection.GeneratedProtocolMessageType('_PublishRequest', (_message.Message,), {
  'DESCRIPTOR' : __PUBLISHREQUEST,
  '__module__' : 'cachepubsub_pb2'
  # @@protoc_insertion_point(class_scope:cache_client.pubsub._PublishRequest)
  })
_sym_db.RegisterMessage(_PublishRequest)

_SubscriptionRequest = _reflection.GeneratedProtocolMessageType('_SubscriptionRequest', (_message.Message,), {
  'DESCRIPTOR' : __SUBSCRIPTIONREQUEST,
  '__module__' : 'cachepubsub_pb2'
  # @@protoc_insertion_point(class_scope:cache_client.pubsub._SubscriptionRequest)
  })
_sym_db.RegisterMessage(_SubscriptionRequest)

_SubscriptionItem = _reflection.GeneratedProtocolMessageType('_SubscriptionItem', (_message.Message,), {
  'DESCRIPTOR' : __SUBSCRIPTIONITEM,
  '__module__' : 'cachepubsub_pb2'
  # @@protoc_insertion_point(class_scope:cache_client.pubsub._SubscriptionItem)
  })
_sym_db.RegisterMessage(_SubscriptionItem)

_TopicItem = _reflection.GeneratedProtocolMessageType('_TopicItem', (_message.Message,), {
  'DESCRIPTOR' : __TOPICITEM,
  '__module__' : 'cachepubsub_pb2'
  # @@protoc_insertion_point(class_scope:cache_client.pubsub._TopicItem)
  })
_sym_db.RegisterMessage(_TopicItem)

_TopicValue = _reflection.GeneratedProtocolMessageType('_TopicValue', (_message.Message,), {
  'DESCRIPTOR' : __TOPICVALUE,
  '__module__' : 'cachepubsub_pb2'
  # @@protoc_insertion_point(class_scope:cache_client.pubsub._TopicValue)
  })
_sym_db.RegisterMessage(_TopicValue)

_Discontinuity = _reflection.GeneratedProtocolMessageType('_Discontinuity', (_message.Message,), {
  'DESCRIPTOR' : __DISCONTINUITY,
  '__module__' : 'cachepubsub_pb2'
  # @@protoc_insertion_point(class_scope:cache_client.pubsub._Discontinuity)
  })
_sym_db.RegisterMessage(_Discontinuity)

_Heartbeat = _reflection.GeneratedProtocolMessageType('_Heartbeat', (_message.Message,), {
  'DESCRIPTOR' : __HEARTBEAT,
  '__module__' : 'cachepubsub_pb2'
  # @@protoc_insertion_point(class_scope:cache_client.pubsub._Heartbeat)
  })
_sym_db.RegisterMessage(_Heartbeat)

_PUBSUB = DESCRIPTOR.services_by_name['Pubsub']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030grpc.cache_client.pubsubP\001Z0github.com/momentohq/client-sdk-go;client_sdk_go\252\002!Momento.Protos.CacheClient.Pubsub'
  __PUBLISHREQUEST._options = None
  __PUBLISHREQUEST._serialized_options = b'\200\265\030\000'
  __SUBSCRIPTIONREQUEST._options = None
  __SUBSCRIPTIONREQUEST._serialized_options = b'\200\265\030\001'
  __EMPTY._serialized_start=60
  __EMPTY._serialized_end=68
  __PUBLISHREQUEST._serialized_start=70
  __PUBLISHREQUEST._serialized_end=177
  __SUBSCRIPTIONREQUEST._serialized_start=179
  __SUBSCRIPTIONREQUEST._serialized_end=283
  __SUBSCRIPTIONITEM._serialized_start=286
  __SUBSCRIPTIONITEM._serialized_end=478
  __TOPICITEM._serialized_start=480
  __TOPICITEM._serialized_end=572
  __TOPICVALUE._serialized_start=574
  __TOPICVALUE._serialized_end=629
  __DISCONTINUITY._serialized_start=631
  __DISCONTINUITY._serialized_end=704
  __HEARTBEAT._serialized_start=706
  __HEARTBEAT._serialized_end=718
  _PUBSUB._serialized_start=721
  _PUBSUB._serialized_end=905
# @@protoc_insertion_point(module_scope)