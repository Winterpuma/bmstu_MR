import networkx as nx
import matplotlib.pyplot as plt

EPS = 1e-3


def convert_matrix_to_nx_form(matr):
    res = []
    for i_row in range(len(matr)):
        for i_col in range(len(matr[i_row])):
            cur = matr[i_row][i_col]
            if cur > EPS:
                res.append((i_row, i_col, cur))
    return res


def graph(matr):
    DG = nx.DiGraph()
    DG.add_weighted_edges_from(convert_matrix_to_nx_form(matr))
    pos = nx.circular_layout(DG)
    nx.draw(DG, pos, with_labels=True)
    labels = nx.get_edge_attributes(DG, 'weight')
    nx.draw_networkx_edge_labels(DG, pos, edge_labels=labels, label_pos=0.2)
    plt.show()


def graph_probability_over_time(probabilities, stabilization_time, times, probabilities_over_time):
    for i_node in range(len(probabilities_over_time[0])):
        plt.plot(times, [i[i_node] for i in probabilities_over_time])
        plt.scatter(stabilization_time[i_node], probabilities[i_node])

    plt.legend(range(len(probabilities)))
    plt.xlabel('time')
    plt.ylabel('probability')
    plt.show()


if __name__ == '__main__':
    m1 = [[0, 2, 0, 3, 8], [0, 0, 3, 0, 0], [0, 4, 0, 0, 0], [0, 0, 5, 0, 2], [7, 0, 4, 0, 0]]
    m2 = [[0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 3], [3, 0, 0, 0]]
    m3 = [[0, 0.7525, 0.2761], [0.1805, 0., 0.3038], [0.536,  0.9106, 0.]]
    graph(m3)
