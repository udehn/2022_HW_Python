import math
import matplotlib.pyplot as plt
import numpy as np


def func(x):
    return math.sin(x)


def get_func_derivative_list(step, F, X):
    return [(F(xi+step)-F(xi-step))/(step*2) for xi in X]


if __name__ == "__main__":
    # граф функции
    x = list(np.arange(-10, 10, 0.01))
    y = [func(xi) for xi in x]
    plt.title("График функции")
    plt.plot(x, y)
    plt.show()

    # граф производной функции
    step = 0.0001
    y2 = get_func_derivative_list(step, func, x)
    plt.title("График производной функции")
    plt.plot(x, y2)
    plt.show()


