
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

titles = ['empty Send and Return',
          'int32 Send and Return',
          'double Send and Return',
          'multiInt32 Send and Return']

titles.extend([f'string_{i} Send and Return' for i in range(10)])

rfiles = [f'time_taken_rpyc__500_{i}.csv' for i in range(1, 6)]
gfiles = [f'time_taken_grpc__500_{i}.csv' for i in range(1, 6)]

directories = [(f'log/{sub_dir}/grpc_log', f'log/{sub_dir}/rpyc_log')
               for sub_dir in ['other_log', 'remote_log', 'local_log']]


def file_name(dir, filename):
    return f"{dir}/{filename}"


def get_data(data):
    if data == '':
        return
    return [float(time_point)
            for time_point in data.split(',')]


def plot_jux_graph(file, file_2, output_dir, title=''):

    time = get_data(file.readline())
    time_2 = get_data(file_2.readline())

    fig, ax = plt.subplots(layout="constrained")
    plt.plot(time, label='grpc')
    plt.plot(time_2, label='rpyc')

    ax.add_artist(plt.legend(loc='upper left', title='Graph legend'))

    legend_handles = [
        mpatches.Patch(color='blue', label='grpc'),
        mpatches.Patch(color='orange', label='rpyc'),
    ]

    legend = plt.legend(handles=legend_handles,
                        loc='upper right',
                        title='Statistics')

    legend.get_texts()[0].set_text(
            f'Mean={np.mean(time)}\nStd={np.std(time)}')
    legend.get_texts()[1].set_text(
            f'Mean={np.mean(time_2)}\nStd={np.std(time_2)}')

    plt.title(f'grpc x rpyc {title}')
    plt.ylabel('Time taken (seconds)')
    plt.xlabel('Iteration')
    plt.ylim(0, max(max(time), max(time_2)))

    plt.savefig(f"{output_dir}/{title}")
    plt.close(fig)


def plotting_comp(file, file_2, plot_method, title_list, output_dir):
    with open(file, 'r') as fd:
        with open(file_2, 'r') as fd_2:
            for title in title_list:
                plot_method(fd, fd_2, output_dir, title)


def bar_plot(file_list,
             file_with_path_list,
             labels,
             output_dir,
             aggr_function):

    size = len(labels)
    experiment = [f'ex_{i}' for i in range(size)]
    data_list = [[] for i in range(size)]
    k = 0

    for file in file_with_path_list:
        k = 0
        with open(file, 'r') as f:
            while True:
                buff = get_data(f.readline())
                if not buff:
                    break
                data_list[k].append(aggr_function(buff))
                k += 1

    x = np.arange(1)
    width = 0.1
    idx_label = 0

    for data, file_name in zip(data_list, labels):

        fig, ax = plt.subplots(layout="constrained")
        i = 0

        for data_value in data:
            offset = width * i
            ax.bar(x + offset, data_value, width, label=experiment[i])
            i += 1

        if np.mean == aggr_function:
            ax.set_ylabel('Mean of time (seconds)')
            ax.set_title('Grouped means')
        elif np.std == aggr_function:
            ax.set_ylabel('Stddev of time (seconds)')
            ax.set_title('Grouped stddev')

        ax.legend(ncols=5, loc='upper left')
        ax.set_xticks(x + width, [labels[idx_label]])
        plt.savefig(f"{output_dir}/{file_name}")
        plt.close(fig)
        idx_label += 1


def main():

    mode = input('(g)raph or (b)ar\nInput the mode: ')

    if mode == 'g':
        for directory in directories:
            print(directory)
            for file in zip(gfiles, rfiles):
                output = f"bar{directory[0].strip('log')}_x_rpyc_bar"

                os.makedirs(output, exist_ok=True)

                plotting_comp(file_name(directory[0],
                                        file[0]),
                              file_name(directory[1],
                                        file[1]),
                              plot_jux_graph,
                              titles,
                              output)
    elif mode == 'b':
        for directory in directories:

            output_dir = f"graph{directory[0].strip('log')}graph/mean"
            os.makedirs(output_dir,
                        exist_ok=True)
            bar_plot(gfiles,
                     [file_name(directory[0], file)
                      for file in gfiles],
                     titles,
                     output_dir,
                     np.mean)

            output_dir = f"graph{directory[0].strip('log')}graph/stdev"
            os.makedirs(output_dir,
                        exist_ok=True)
            bar_plot(gfiles,
                     [file_name(directory[0], file)
                      for file in gfiles],
                     titles,
                     output_dir,
                     np.std)

            output_dir = f"graph{directory[1].strip('log')}graph/mean"
            os.makedirs(output_dir,
                        exist_ok=True)
            bar_plot(rfiles,
                     [file_name(directory[1], file)
                      for file in rfiles],
                     titles,
                     output_dir,
                     np.mean)

            output_dir = f"graph{directory[1].strip('log')}graph/stdev"
            os.makedirs(output_dir,
                        exist_ok=True)
            bar_plot(rfiles,
                     [file_name(directory[1], file)
                      for file in rfiles],
                     titles,
                     output_dir,
                     np.std)
    else:
        print('Please input a valid option')


if __name__ == "__main__":
    main()
