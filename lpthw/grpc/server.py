import grpc
from concurrent import futures
import time

#importing the generated class from grpc
import palindrome_pb2
import palindrome_pb2_grpc

import palindrome

class PalindromeCheckerServicer(palindrome_pb2_grpc.PalindromeCheckerServicer):
    def isPalindrome(self,request,context):
        response=palindrome_pb2.InputCheckResponse()
        response.value=palindrome.isPalindrome(request.value)
        return response

# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the server
palindrome_pb2_grpc.add_PalindromeCheckerServicer_to_server(
        PalindromeCheckerServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)