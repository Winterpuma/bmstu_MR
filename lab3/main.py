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


if __name__ == '__main__':
    matr = generate_matrix(4)

    # Вывод графа связей и весов
    graph.graph(matr)

    # Нахождение предельных вероятностей
    probability = solve_linalg.solve(matr)
    output('Предельные вероятности:', 'p', probability)

    # Нахождение времени стабилизации
    stabilization_time = stabilization.calc_stabilization_times(matr, [1, 0, 0, 0, 0], probability)
    output('Время стабилизации:', 't', stabilization_time)
