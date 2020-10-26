import matplotlib.pyplot as plt
import numpy as np
from random import randint


def fill_arr(func, arr, n, start, stop):
    for i in range(n):
        a = func(start, stop)
        #print(a)
        arr[a - start] += 1

def graph():
    start = 0
    stop = 10
    n = 1000

    expected_avg = n / (stop - start)
    
    orig = [0] * (stop - start)
    orig2 = [0] * (stop - start)
    fill_arr(randint, orig, n, start, stop - 1)
    fill_arr(np.random.randint, orig2, n, start, stop)

    print(orig)
    plt.figure(1)
    plt.ylabel("amount")
    plt.xlabel("generated number")
    
    plt.axis((start - 1, stop, 0, expected_avg * 2))

    plt.stem(range(start, stop), orig, bottom=expected_avg,
             linefmt='grey', markerfmt='D')
    plt.stem(range(start, stop), orig2, bottom=expected_avg,
             linefmt='grey', markerfmt='D')
    
    plt.show()

graph()
