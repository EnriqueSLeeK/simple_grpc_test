
import os


def naming(file_name):
    diff = 1
    while True:
        tmp = f'{file_name}_{diff}.csv'
        if os.path.isfile(tmp):
            diff += 1
        else:
            return tmp


def to_str_time(time_list):
    return ",".join(str(time) for time in time_list)


def write_files(dir, file_name, iteration, time_taken, i):
    print('Writing to log')
    os.makedirs(dir, exist_ok=True)
    with open(f"{naming(f'{dir}/{file_name}')}",
              "w") as csv:
        csv.write(f"{to_str_time(time_taken['empty'])}\n")
        csv.write(f"{to_str_time(time_taken['int32'])}\n")
        csv.write(f"{to_str_time(time_taken['double'])}\n")
        csv.write(f"{to_str_time(time_taken['multiInt32'])}\n")
        for k in range(i):
            csv.write(f"{to_str_time(time_taken[f'string_{k}'])}\n")
