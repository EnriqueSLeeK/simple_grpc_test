
import matplotlib.pyplot as plt


def plot_graph(file, title=''):
    time = []

    time.extend(
            [float(time_point)
                for time_point in file.readline().split(',')]
            )

    plt.title(title)
    plt.ylabel('Time taken')
    plt.xlabel('Iteration')
    plt.plot(time)
    plt.show()


def main():
    with open('log/time_taken_rpyc.csv', 'r') as file:
        plot_graph(file, 'rpyc - Empty send and return')
        plot_graph(file, 'rpyc - Long send and return')
        plot_graph(file, 'rpyc - Double send and return')
        plot_graph(file, 'rpyc - MultiLongToOne send and return')

    with open('log/time_taken_grpc.csv', 'r') as file:
        plot_graph(file, 'grpc - Empty send and return')
        plot_graph(file, 'grpc - Long send and return')
        plot_graph(file, 'grpc - Double send and return')
        plot_graph(file, 'grpc - MultiLongToOne send and return')


if __name__ == "__main__":
    main()
