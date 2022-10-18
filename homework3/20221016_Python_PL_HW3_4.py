import matplotlib.pyplot as plt
import numpy as np


def func(x, y):
    return x**2-y**2


def get_surface():
    ax3 = plt.axes(projection='3d')
    x = np.arange(-1, 1, 0.1)
    y = np.arange(-1, 1, 0.1)
    X, Y = np.meshgrid(x, y)
    Z = func(X, Y)
    ax3.plot_surface(X, Y, Z, cmap='rainbow')
    plt.title("Граф функции")
    plt.show()


def get_directional_field():
    x = np.arange(-1, 1, 0.1)
    y = np.arange(-1, 1, 0.1)
    X, Y = np.meshgrid(x, y)
    y2 = func(X, Y)
    x2 = np.ones(y2.shape)
    plt.quiver(X, Y, x2, y2, color="black")
    plt.title("Граф поле направлений")
    plt.show()


if __name__ == "__main__":
    get_surface()
    get_directional_field()
