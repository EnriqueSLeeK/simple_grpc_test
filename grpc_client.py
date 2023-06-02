
import time
import grpc
import proto_files.grpc_service_pb2 as grpc_service_pb2
import proto_files.grpc_service_pb2_grpc as grpc_service_pb2_grpc


time_taken = {
        'empty': [],
        'int32': [],
        'double': [],
        'string': []
        }


def print_status(status):
    print(f"Test: status {status}")


def emptyTest(stub):
    data = grpc_service_pb2.Empty()
    start = time.time()
    for i in range(1000):
        stub.emptyReturn(data)
    end = time.time()
    time_taken['empty'].append(end - start)


def stringTest(stub):
    for i in range(10):
        string = 'aaaaa' * pow(4, i)
        data = grpc_service_pb2.stringData(string_data=string)
        start = time.time()
        for k in range(1000):
            stub.stringReturn(data)
        end = time.time()
        time_taken['string'].append(end - start)


def int32Test(stub):
    data = grpc_service_pb2.int32Data(int32_data=123)
    start = time.time()
    for k in range(1000):
        stub.int32Return(data)
    end = time.time()
    time_taken['int32'].append(end - start)


def doubleTest(stub):
    data = grpc_service_pb2.doubleData(double_data=111111.1111111)
    start = time.time()
    for k in range(1000):
        stub.doubleReturn(data)
    end = time.time()
    time_taken['double'].append(end - start)


def main():
    channel = grpc.insecure_channel('[::]:50051')
    stub = grpc_service_pb2_grpc.serviceTestStub(channel)

    emptyTest(stub)
    stringTest(stub)
    int32Test(stub)
    doubleTest(stub)

    print(time_taken)


if __name__ == "__main__":
    main()
