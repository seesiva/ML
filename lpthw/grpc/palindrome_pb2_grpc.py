# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import palindrome_pb2 as palindrome__pb2


class PalindromeCheckerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.isPalindrome = channel.unary_unary(
        '/PalindromeChecker/isPalindrome',
        request_serializer=palindrome__pb2.InputCheckString.SerializeToString,
        response_deserializer=palindrome__pb2.InputCheckResponse.FromString,
        )


class PalindromeCheckerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def isPalindrome(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PalindromeCheckerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'isPalindrome': grpc.unary_unary_rpc_method_handler(
          servicer.isPalindrome,
          request_deserializer=palindrome__pb2.InputCheckString.FromString,
          response_serializer=palindrome__pb2.InputCheckResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'PalindromeChecker', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
