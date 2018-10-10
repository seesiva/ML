import grpc

# import the generated classes
import palindrome_pb2
import palindrome_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = palindrome_pb2_grpc.PalindromeCheckerStub(channel)

# create a valid request message
requestString = palindrome_pb2.InputCheckString(value="woon")

# make the call
response = stub.isPalindrome(requestString)

# et voilà
print(response.value)