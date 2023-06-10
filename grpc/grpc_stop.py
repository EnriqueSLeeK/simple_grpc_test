
import grpc
import proto_files.grpc_service_pb2 as grpc_service_pb2
import proto_files.grpc_service_pb2_grpc as grpc_service_pb2_grpc

channel = grpc.insecure_channel('[::]:50051')
stub = grpc_service_pb2_grpc.serviceTestStub(channel)
stub.shutdown(grpc_service_pb2.Empty())
