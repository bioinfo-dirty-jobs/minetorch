# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from minetorch.proto import minetorch_pb2 as minetorch_dot_proto_dot_minetorch__pb2


class MinetorchStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.HeyYo = channel.unary_unary(
        '/minetorch.Minetorch/HeyYo',
        request_serializer=minetorch_dot_proto_dot_minetorch__pb2.HeyMessage.SerializeToString,
        response_deserializer=minetorch_dot_proto_dot_minetorch__pb2.YoMessage.FromString,
        )
    self.SendLog = channel.unary_unary(
        '/minetorch.Minetorch/SendLog',
        request_serializer=minetorch_dot_proto_dot_minetorch__pb2.Log.SerializeToString,
        response_deserializer=minetorch_dot_proto_dot_minetorch__pb2.StandardResponse.FromString,
        )
    self.SetTimer = channel.unary_unary(
        '/minetorch.Minetorch/SetTimer',
        request_serializer=minetorch_dot_proto_dot_minetorch__pb2.Timer.SerializeToString,
        response_deserializer=minetorch_dot_proto_dot_minetorch__pb2.StandardResponse.FromString,
        )
    self.AddPoint = channel.unary_unary(
        '/minetorch.Minetorch/AddPoint',
        request_serializer=minetorch_dot_proto_dot_minetorch__pb2.Point.SerializeToString,
        response_deserializer=minetorch_dot_proto_dot_minetorch__pb2.StandardResponse.FromString,
        )
    self.CreateGraph = channel.unary_unary(
        '/minetorch.Minetorch/CreateGraph',
        request_serializer=minetorch_dot_proto_dot_minetorch__pb2.Graph.SerializeToString,
        response_deserializer=minetorch_dot_proto_dot_minetorch__pb2.StandardResponse.FromString,
        )


class MinetorchServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def HeyYo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendLog(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetTimer(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddPoint(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateGraph(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MinetorchServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'HeyYo': grpc.unary_unary_rpc_method_handler(
          servicer.HeyYo,
          request_deserializer=minetorch_dot_proto_dot_minetorch__pb2.HeyMessage.FromString,
          response_serializer=minetorch_dot_proto_dot_minetorch__pb2.YoMessage.SerializeToString,
      ),
      'SendLog': grpc.unary_unary_rpc_method_handler(
          servicer.SendLog,
          request_deserializer=minetorch_dot_proto_dot_minetorch__pb2.Log.FromString,
          response_serializer=minetorch_dot_proto_dot_minetorch__pb2.StandardResponse.SerializeToString,
      ),
      'SetTimer': grpc.unary_unary_rpc_method_handler(
          servicer.SetTimer,
          request_deserializer=minetorch_dot_proto_dot_minetorch__pb2.Timer.FromString,
          response_serializer=minetorch_dot_proto_dot_minetorch__pb2.StandardResponse.SerializeToString,
      ),
      'AddPoint': grpc.unary_unary_rpc_method_handler(
          servicer.AddPoint,
          request_deserializer=minetorch_dot_proto_dot_minetorch__pb2.Point.FromString,
          response_serializer=minetorch_dot_proto_dot_minetorch__pb2.StandardResponse.SerializeToString,
      ),
      'CreateGraph': grpc.unary_unary_rpc_method_handler(
          servicer.CreateGraph,
          request_deserializer=minetorch_dot_proto_dot_minetorch__pb2.Graph.FromString,
          response_serializer=minetorch_dot_proto_dot_minetorch__pb2.StandardResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'minetorch.Minetorch', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
