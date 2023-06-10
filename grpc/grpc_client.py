
import time
import grpc
import file_operation.operation.file_op as fop
import proto_files.grpc_service_pb2 as grpc_service_pb2
import proto_files.grpc_service_pb2_grpc as grpc_service_pb2_grpc


channel = grpc.insecure_channel('[::]:50051')
stub = grpc_service_pb2_grpc.serviceTestStub(channel)

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


def time_test(type_tested, remote_method, data, iteration):
    time_taken[type_tested].extend(
            test(remote_method, data, iteration)
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


def check_and_parse(number):
    if number.isdigit() and number[0] not in ('+', '-'):
        return int(number)
    print('Bad iteration input defaulting number of iteration')
    return 2000


def empty_content_from_associate_value():
    for i in time_taken:
        time_taken[i] = []


def main():
    iteration = check_and_parse(input('Numero de iteracoes: '))

    print('empty test')
    time_test("empty",
              stub.emptyReturn,
              empty(),
              iteration)

    print('double test')
    time_test("int32",
              stub.int32Return,
              int32(),
              iteration)

    print('int32 test')
    time_test("double",
              stub.doubleReturn,
              double(),
              iteration)

    print('multiInt32 test')
    time_test("multiInt32",
              stub.int32MultiToOneReturn,
              multiInt(),
              iteration)

    data_list = string()
    i = 0
    for data in data_list:
        print(f'string_{i} test')
        time_test(f"string_{i}",
                  stub.stringReturn,
                  data,
                  iteration)
        i += 1

    fop.write_files('../grpc_log',
                    f'time_taken_grpc__{iteration}',
                    iteration,
                    time_taken,
                    i)

    empty_content_from_associate_value()


if __name__ == "__main__":
    main()
