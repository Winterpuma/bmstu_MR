import matplotlib.pyplot as plt
from math import sqrt
from scipy.stats import norm
import numpy as np


def ud_function(a, b, x):
    return (x - a) / (b - a) if a <= x < b else 0 if x < a else 1


def ud_density(a, b, x):
    return 1 / (b - a) if a <= x <= b else 0


def norm_function(x, mu, sigma):
    return norm.cdf(x, mu, sqrt(sigma))


def norm_density(x, mu, sigma):
    return norm.pdf(x, mu, sqrt(sigma))


def draw_graphics(x, y_function, y_density, name):
    fig, axs = plt.subplots(2, figsize=(6, 7))

    fig.suptitle(name)
    axs[0].plot(x, y_function, color='purple')
    axs[1].plot(x, y_density, color='purple')

    axs[0].set_xlabel('x')
    axs[0].set_ylabel('F(x)')

    axs[1].set_xlabel('x')
    axs[1].set_ylabel('f(x)')

    axs[0].grid(True)
    axs[1].grid(True)
    plt.show()


def main():
    a = float(input("Input a: "))
    b = float(input("Input b: "))
    delta = b - a
    x = np.arange(a - delta / 2, b + delta / 2, 0.001)
    y_function = [ud_function(a, b, _x) for _x in x]
    y_density = [ud_density(a, b, _x) for _x in x]
    draw_graphics(x, y_function, y_density, 'Равномерное распределение')

    mu = float(input("Input mu: "))
    sigma = float(input("Input sigma: "))
    x = np.arange(-10, 10, 0.001)
    y_function = norm_function(x, mu, sigma)
    y_density = norm_density(x, mu, sigma)

    draw_graphics(x, y_function, y_density, 'Нормальное распределение')


if __name__ == '__main__':
    main()
