
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from statistics import stdev
from statistics import mean


titles = ['empty Send and Return',
          'int32 Send and Return',
          'double Send and Return',
          'multiInt32 Send and Return']

titles.extend([f'string_{i} Send and Return' for i in range(10)])


def get_data(data):
    return [float(time_point)
            for time_point in data.split(',')]


def plot_jux_graph(file, file_2, title=''):

    time = get_data(file.readline())
    time_2 = get_data(file_2.readline())

    plt.subplot()
    plt.plot(time, label='grpc')
    plt.plot(time_2, label='rpyc')

    plt.gca().add_artist(plt.legend(loc='upper left', title='Graph legend'))

    legend_handles = [
        mpatches.Patch(color='blue', label='grpc'),
        mpatches.Patch(color='orange', label='rpyc'),
    ]

    legend = plt.legend(handles=legend_handles,
                        loc='upper right',
                        title='Statistics')
    legend.get_texts()[0].set_text(
            f'Mean={mean(time)}\nStd={stdev(time)}')
    legend.get_texts()[1].set_text(
            f'Mean={mean(time_2)}\nStd={stdev(time_2)}')

    plt.title(f'grpc x rpyc {title}')
    plt.ylabel('Time taken')
    plt.xlabel('Iteration')
    plt.savefig(f'graph/{title}.png')
    plt.show()


def plot_two_graph(file, file_2, title=''):
    time = get_data(file.readline())
    # time_2 = get_data(file_readline())
    print(time)


def file_name(dir, filename):
    return f"{dir}/{filename}"


def plotting(file, file_2, plot_method, title_list):
    with open(file, 'r') as fd:
        with open(file_2, 'r') as fd_2:
            for title in title_list:
                plot_method(fd, fd_2, title)


def main():
    plotting(file_name('grpc_log', 'time_taken_grpc_2000.csv'),
             file_name('rpyc_log', 'time_taken_rpyc_2000.csv'),
             plot_jux_graph,
             titles)
    """
    plotting(file_name('result', 'time_taken_grpc_2000.csv'),
             file_name('result', 'time_taken_rpyc_2000.csv'),
             plot_jux_graph,
             titles)
    """


if __name__ == "__main__":
    main()
