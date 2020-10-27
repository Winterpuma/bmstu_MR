import matplotlib.pyplot as plt
import numpy as np
from random import randint

import PRNG_table
import PRNG_algo

def fill_arr(func, arr_counter, arr, n, start, stop):
    for i in range(n):
        a = func(start, stop)
        #print(a)
        arr_counter[a - start] += 1
        arr.append(a)

def graph(start, stop, n, func):
    expected_avg = n / (stop - start)
    
    counter = [0] * (stop - start)
    res = []

    fill_arr(func, counter, res, n, start, stop - 1)
    plt.figure(1)
    plt.axis((start - 1, stop, 0, expected_avg * 2))
    plt.stem(range(start, stop), counter, bottom=expected_avg,
             linefmt='grey', markerfmt='D')

    plt.figure(2)
    plt.hist(res, (stop - start))

    plt.figure(3)
    #plt.axis(0, n, start - 1, stop + 1)
    plt.plot(range(n), res, "o")
    
    


def start():
    start = 0
    stop = 100
    n = 10000

    plt.ylabel("amount")
    plt.xlabel("generated number")

    a = PRNG_table.Table("even_table.txt")
    graph(start, stop, n, a.next)    
    
    #graph(start, stop, n, randint) # [)
    #graph(start, stop, n, np.random.randint)

    #b = PRNG_algo.LinearCongruent()
    #graph(start, stop, n, b.next)

    plt.show()

    


start()
