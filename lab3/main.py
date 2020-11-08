from math import fabs
import random

import graph
import solve_linalg
import stabilization

PRECISION = 5


def generate_matrix(size):
    return [
        [round(random.random(), PRECISION) if i != j else 0.0 for j in range(size)]
        for i in range(size)
    ]


def output(title, caption, data):
    print(title)
    for i in range(len(data)):
        print(caption + str(i), round(fabs(data[i]), PRECISION))
    print()


def get_pre_def_intensity(i):
    if i == 4:
        return [[0, 2, 0, 0],
                [0, 0, 3, 0],
                [0, 0, 0, 3],
                [3, 0, 0, 0]]
    elif i == 5:
        return [[0, 0.5, 0, 0, 0],
                [0, 0, 2, 0, 0],
                [0, 0, 0, 1.5, 1.5],
                [0.8, 0, 0, 0, 0],
                [2, 0, 0, 0, 0]]
    else:
        raise KeyError('No pre def intensity for i == ' + str(i))


def get_start_probabilities(n, all_equal=True):
    if all_equal:
        return [1/n] * n
    else:
        res = [0] * n
        res[0] = 1
        return res


if __name__ == '__main__':
    n = 5
    #intensity = generate_matrix(n)
    intensity = get_pre_def_intensity(n)

    start_probabilities = get_start_probabilities(n, False)

    # Нахождение предельных вероятностей
    probability = solve_linalg.solve(intensity)
    output('Предельные вероятности:', 'p', probability)

    # Нахождение времени стабилизации
    stabilization_time = stabilization.calc_stabilization_times(intensity, start_probabilities, probability)
    times, probabilities_over_time = stabilization.calc_probability_over_time(intensity, start_probabilities, 5)
    output('Время стабилизации:', 't', stabilization_time)

    # Вывод графа связей и весов
    graph.graph(intensity)
    # Вывод графиков вероятностей как функции времени
    graph.graph_probability_over_time(probability, stabilization_time, times, probabilities_over_time)
