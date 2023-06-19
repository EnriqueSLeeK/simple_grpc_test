
from concurrent import futures

import grpc
import proto_files.grpc_service_pb2 as grpc_service_pb2
import proto_files.grpc_service_pb2_grpc as grpc_service_pb2_grpc


class serviceTest(grpc_service_pb2_grpc.serviceTest):

    def emptyReturn(self, request, context):
        return_data = grpc_service_pb2.Empty()
        return return_data

    def doubleReturn(self, request, context):
        return_data = grpc_service_pb2.doubleData(
                double_data=request.double_data)
        return return_data

    def int32Return(self, request, context):
        return_data = grpc_service_pb2.int32Data(
                int32_data=request.int32_data)
        return return_data

    def int32MultiToOneReturn(self, request, context):
        return_data = grpc_service_pb2.int32Data(
                int32_data=request.int32_d_0)
        return return_data

    def stringReturn(self, request, context):
        return_data = grpc_service_pb2.stringData(
                string_data=request.string_data)
        return return_data

    def customObjectReturn(self, request, context):
        return_data = grpc_service_pb2.customObject(
                custom_data=request.custom_data)
        return return_data

    def shutdown(self, request, context):
        server.stop(0)
        return request


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
grpc_service_pb2_grpc.add_serviceTestServicer_to_server(
    serviceTest(), server)
server.add_insecure_port('[::]:50051')
print("Start server")
server.start()
server.wait_for_termination()
