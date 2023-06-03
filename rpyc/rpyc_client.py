
import os
import time
import rpyc


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

conn = rpyc.connect('localhost', 18811)


def test(remote_method, data, iterations=2000):
    time_measure = []
    for i in range(iterations):
        start = time.time()
        remote_method(data)
        end = time.time()
        time_measure.append(end - start)
    return time_measure


def time_test(type_tested, remote_method, data):
    time_taken[type_tested].extend(
        test(remote_method, data)
        )


def string():
    data = []
    for i in range(10):
        data.append('aaaaa' * pow(4, i))
    return data


def to_str_time(time_list):
    return ",".join(str(time) for time in time_list)


def main():
    time_test('empty', conn.root.valueReturn, None)

    data_string = string()
    i = 0
    for data in data_string:
        time_test(f'string_{i}', conn.root.valueReturn, data)
        i += 1

    time_test('multiInt32', conn.root.valueReturn, [1, 2,
                                                    3, 4,
                                                    5, 6,
                                                    7, 8])

    time_test('double', conn.root.valueReturn, 111111.1111111)

    time_test('int32', conn.root.valueReturn, 123)

    os.makedirs('../log', exist_ok=True)

    with open("../log/time_taken_rpyc.csv", "w") as csv:
        csv.write(f"void,{to_str_time(time_taken['empty'])}\n")
        csv.write(f"long,{to_str_time(time_taken['int32'])}\n")
        for i in range(10):
            csv.write(f"string_{i},{to_str_time(time_taken[f'string_{i}'])}\n")
        csv.write(f"double,{to_str_time(time_taken['double'])}\n")


if __name__ == "__main__":
    main()
