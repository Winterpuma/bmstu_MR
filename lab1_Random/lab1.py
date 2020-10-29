import matplotlib.pyplot as plt
import numpy as np
from random import randint

import PRNG_table
import PRNG_algo
import criterion


def fill_arr(func, seq, cnt, n, start, stop):
    for i in range(n):
        a = func(start, stop)
        seq.append(a)
        cnt[a - start] += 1


def graph(expected_avg, cnt, seq):
    plt.figure(1)
    plt.axis((start - 1, stop, 0, expected_avg * 2))
    plt.stem(range(start, stop), cnt, bottom=expected_avg,
             linefmt='grey', markerfmt='D')

    plt.figure(2)
    plt.hist(seq, (stop - start))

    plt.figure(3)
    plt.plot(range(n), seq, "o")


def generate_and_graph(func):
    expected_avg = n / (stop - start)

    seq = []
    cnt = [0] * (stop - start)

    fill_arr(func, seq, cnt, n, start, stop - 1)

    print('p-value: {:.7f}'.format(float(criterion.chi2_criterion(cnt))))
    print('Критерий промежутков между днями рождения: R =', criterion.bday_criterion(cnt))

    plt.ylabel("amount")
    plt.xlabel("generated number")
    graph(expected_avg, cnt, seq)
    plt.show()



def go(i):
    if i == 0:
        generate_and_graph(randint)
    elif i == 1:
        lin_cong = PRNG_algo.LinearCongruent()
        generate_and_graph(lin_cong.next)
    elif i == 2:
        filename = "only5-9.txt"
        # count_digits_in_file(filename)
        my_table = PRNG_table.MyTableMethod(filename)
        generate_and_graph(my_table.next)


def count_digits_in_file(filename):
    data = ""
    f = open(filename)
    for line in f.read().split('\n'):
        data += line
    f.close()

    for i in range(10):
        print(i, data.count(str(i)))

    print('Total len', len(data))


start = 0
stop = 5
n = 100

go(2)
