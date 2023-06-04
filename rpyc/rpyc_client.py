
import os
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


def time_test(type_tested, remote_method, data):
    time_taken[type_tested].extend(
        test(remote_method, data)
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


def main():
    print('empty test')
    time_test('empty',
              conn.root.valueReturn,
              empty())

    print('double test')
    time_test('double',
              conn.root.valueReturn,
              double())

    print('int32 test')
    time_test('int32',
              conn.root.valueReturn,
              int32())

    print(multiInt().data_0)
    print('multiInt32 test')
    time_test('multiInt32',
              conn.root.multiToOneReturn,
              multiInt())

    data_string = string()
    i = 0
    for data in data_string:
        print(f'string_{i} test')
        time_test(f'string_{i}',
                  conn.root.valueReturn,
                  data)
        i += 1

    print('Writing to log')
    os.makedirs('../log', exist_ok=True)

    with open("../log/time_taken_rpyc.csv", "w") as csv:
        csv.write(f"{to_str_time(time_taken['empty'])}\n")
        csv.write(f"{to_str_time(time_taken['int32'])}\n")
        csv.write(f"{to_str_time(time_taken['double'])}\n")
        csv.write(f"{to_str_time(time_taken['multiInt32'])}\n")
        for i in range(i):
            csv.write(f"{to_str_time(time_taken[f'string_{i}'])}\n")


if __name__ == "__main__":
    main()
