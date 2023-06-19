
import numpy as np
import os

titles = ['empty Send and Return',
          'int32 Send and Return',
          'double Send and Return',
          'multiInt32 Send and Return']

titles.extend([f'string_{i} Send and Return' for i in range(10)])

rfiles = [f'time_taken_rpyc__500_{i}.csv' for i in range(1, 6)]
gfiles = [f'time_taken_grpc__500_{i}.csv' for i in range(1, 6)]

dir = ['other_log', 'remote_log', 'local_log']

directories = [(f'log/{sub_dir}/grpc_log', f'log/{sub_dir}/rpyc_log')
               for sub_dir in dir]

titles = ['empty Send and Return',
          'int32 Send and Return',
          'double Send and Return',
          'multiInt32 Send and Return']

titles.extend([f'string_{i} Send and Return' for i in range(10)])


def file_name(dir, filename):
    return f"{dir}/{filename}"


def get_data(data):
    if data == '':
        return
    return [float(time_point)
            for time_point in data.split(',')]


def get_ratio(fd, fd_2, titles_list):
    ratio_list = []
    for title in titles_list:
        grpc = np.sum(get_data(fd.readline()))
        rpyc = np.sum(get_data(fd_2.readline()))
        ratio_list.append(grpc / rpyc)
    return ratio_list


def calculate_ratio(file, file_2):
    with open(file, 'r') as fd:
        with open(file_2, 'r') as fd_2:
            return get_ratio(fd, fd_2, titles)


def to_str(data_list):
    return ",".join(str(data) for data in data_list)


def to_str_trunc(data_list):
    return ",".join(str(data)[:6] for data in data_list)


def main():
    ratio_list = []
    k = 0
    for directory in directories:
        for file in zip(gfiles, rfiles):
            ratio_list.append(
                    calculate_ratio(
                        file_name(directory[0], file[0]),
                        file_name(directory[1], file[1]))
                    )
        output_dir = f"ratio{directory[0].strip('log')}ratio"

        os.makedirs(output_dir, exist_ok=True)
        with open(output_dir + '/data.csv', 'w') as f:
            f.write(f",{to_str(titles)}\n")
            i = 0
            for ratio in ratio_list:
                i += 1
                f.write(f"n{i},{to_str_trunc(ratio)}\n")
        ratio_list = []
        k += 1


if __name__ == "__main__":
    main()
