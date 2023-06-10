
import file_operation.operation.file_op as fop
import time
import rpyc
import classes as c


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

conn = rpyc.connect('localhost', 18811,
                    config={"allow_public_attrs": True})


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
    return c.empty()


def string():
    data = []
    for i in range(10):
        string = 'aaaaa' * pow(4, i)
        data.append(c.genericObj(string))
    return data


def int32():
    return c.genericObj(123)


def double():
    return c.genericObj(111111.1111111)


def multiInt():
    return c.multiObj(1, 2, 3, 4,
                      5, 6, 7, 8)


def to_str_time(time_list):
    return ",".join(str(time) for time in time_list)


def check_and_parse(number):
    print(number)
    if number.isdigit() and number[0] not in ('+', '-'):
        return int(number)
    print('Bad iteration input defaulting number of iteration')
    return 2000


def main():
    iteration = check_and_parse(input('Numero de iteracoes: '))

    print('empty test')
    time_test('empty',
              conn.root.valueReturn,
              empty(),
              iteration)

    print('double test')
    time_test('double',
              conn.root.valueReturn,
              double(),
              iteration)

    print('int32 test')
    time_test('int32',
              conn.root.valueReturn,
              int32(),
              iteration)

    print('multiInt32 test')
    time_test('multiInt32',
              conn.root.multiToOneReturn,
              multiInt(),
              iteration)

    data_string = string()
    i = 0
    for data in data_string:
        print(f'string_{i} test')
        time_test(f'string_{i}',
                  conn.root.valueReturn,
                  data,
                  iteration)
        i += 1

    fop.write_files('../rpyc_log',
                    f'time_taken_rpyc__{iteration}',
                    iteration,
                    time_taken,
                    i)


if __name__ == "__main__":
    main()
