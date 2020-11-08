TIME_DELTA = 1e-3
EPS = 1e-2


def dps(matrix, probabilities):
    n = len(matrix)
    return [
        TIME_DELTA * sum(
            [
                probabilities[j] * (-sum(matrix[i]) + matrix[i][i])
                if i == j else
                probabilities[j] * matrix[j][i]
                for j in range(n)
            ]
        )
        for i in range(n)
    ]


def calc_stabilization_times(matrix, start_probabilities, limit_probabilities):
    n = len(matrix)
    current_time = 0
    current_probabilities = start_probabilities.copy()
    stabilization_times = [0 for i in range(n)]

    lambda_sum = sum([sum(i) for i in matrix])
    cool_eps = [p/lambda_sum for p in limit_probabilities]

    for c in range(10000000):
        curr_dps = dps(matrix, current_probabilities)
        for i in range(n):
            if (
                    not stabilization_times[i] and
                    abs(current_probabilities[i] - limit_probabilities[i]) <= EPS and
                    curr_dps[i] <= EPS
            ):
                stabilization_times[i] = current_time
            current_probabilities[i] += curr_dps[i]
        if all(stabilization_times):
            break
        current_time = round(current_time + TIME_DELTA, 6)
    return stabilization_times
