import matplotlib.pyplot as plt
import numpy as np

lim = 0.000001


def create_graph(x, y, y2, y3, y4):
    plt.ylabel('y')
    plt.xlabel('x')
    plt.plot(x, y)
    plt.plot(x, y2)
    plt.plot(x, y3)
    plt.plot(x, y4, linestyle='dashed')
    plt.title('Derivacao Numerica')
    plt.legend(['progr1', 'central2', '2deriv', 'original'])
    plt.grid()
    plt.show()


def funcao(x):
    return np.sin(x);

def func(x):
    return np.cos(x);


def lista_funcao(x):
    y_list = []

    for num in x:
        y_list.append(func(num))

    return y_list


def finiteDif(x):
    y_list = []
    fx = 0.0

    for num in x:
        aux = 0.1
        while True:
            fx = funcao(num + aux) - funcao(num)

            if aux/10 >= lim:
                aux /= 10
            else:
                break

        y_list.append(fx/aux)

    return y_list


def finitecCentralDif(x):
    y_list = []
    fx = 0.0

    for num in x:
        aux = 0.1
        while True:
            fx = funcao(num + aux) - funcao(num - aux)

            if aux/10 >= lim:
                aux /= 10
            else:
                break

        y_list.append(fx/(2*aux))

    return y_list


def secondDif(x):
    y_list = []
    fx = 0.0

    for num in x:
        aux = 0.1
        while True:
            fx = funcao(num + aux) - 2*funcao(num) + funcao(num - aux)

            if aux/10 >= lim:
                aux /= 10
            else:
                break

        y_list.append(fx/(aux*aux))

    return y_list


if __name__ == '__main__':
    x_list = []
    numero = -3.14
    while numero <= 3.14:
        x_list.append(numero)
        numero += 0.001

    create_graph(x_list, finiteDif(x_list),
            finitecCentralDif(x_list), secondDif(x_list), lista_funcao(x_list))
