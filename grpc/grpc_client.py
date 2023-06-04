
import os
import time
import grpc
import proto_files.grpc_service_pb2 as grpc_service_pb2
import proto_files.grpc_service_pb2_grpc as grpc_service_pb2_grpc


time_taken = {
        'empty': [],
        'int32': [],
        'double': [],
        'string_0': [],
        'string_1': [],
        'string_2': [],
        'string_3': [],
        'string_4': [],
        'string_5': [],
        'string_6': [],
        'string_7': [],
        'string_8': [],
        'string_9': [],
        'multiInt32': [],
        }


def print_status(status):
    print(f"Test: status {status}")


def test(remote_method, data, iterations=2000):
    time_measure = []
    for i in range(iterations):
        if (i % 500) == 0:
            print(i)
        start = time.time()
        remote_method(data)
        end = time.time()
        time_measure.append(end - start)
    return time_measure


def time_test(type_tested, remote_method, data):
    time_taken[type_tested].extend(
        test(remote_method, data)
        )


def empty():
    return grpc_service_pb2.Empty()


def string():
    data = []
    for i in range(10):
        string = 'aaaaa' * pow(4, i)
        data.append(grpc_service_pb2.stringData(string_data=string))
    return data


def int32():
    return grpc_service_pb2.int32Data(int32_data=123)


def double():
    return grpc_service_pb2.doubleData(double_data=111111.1111111)


def multiInt():
    return grpc_service_pb2.int32MultiSend(int32_d_0=1,
                                           int32_d_1=2,
                                           int32_d_2=3,
                                           int32_d_3=4,
                                           int32_d_4=5,
                                           int32_d_5=6,
                                           int32_d_6=7,
                                           int32_d_7=8)


def to_str_time(time_list):
    return ",".join(str(time) for time in time_list)


def main():
    channel = grpc.insecure_channel('[::]:50051')
    stub = grpc_service_pb2_grpc.serviceTestStub(channel)

    print('empty test')
    time_test("empty",
              stub.emptyReturn,
              empty())

    print('double test')
    time_test("int32",
              stub.int32Return,
              int32())

    print('int32 test')
    time_test("double",
              stub.doubleReturn,
              double())

    print('multiInt32 test')
    time_test("multiInt32",
              stub.int32MultiToOneReturn,
              multiInt())

    data_list = string()
    i = 0
    for data in data_list:
        print(f'string_{i} test')
        time_test(f"string_{i}",
                  stub.stringReturn,
                  data)
        i += 1

    os.makedirs('../log', exist_ok=True)

    with open("../log/time_taken_grpc.csv", "w") as csv:
        csv.write(f"{to_str_time(time_taken['empty'])}\n")
        csv.write(f"{to_str_time(time_taken['int32'])}\n")
        csv.write(f"{to_str_time(time_taken['double'])}\n")
        csv.write(f"{to_str_time(time_taken['multiInt32'])}\n")
        for i in range(i):
            csv.write(f"{to_str_time(time_taken[f'string_{i}'])}\n")


if __name__ == "__main__":
    main()
