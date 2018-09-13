"""
    Código para implementar programa que calcula integral definida a partir da regra do trapézio repetid
    Autor: Anthony Louis
    Instituição: Universidade de Brasília
    Ano: 2018
    Método: Trapézio Repetido
"""

import matplotlib.pyplot as plt
import numpy as np


def setup():
    try:
        n = int(input('Insira o numero de intervalos desejados para a integraçao: '))
        x1 = float(input('Insira o limite inferior de integração: '))
        x2 = float(input('Insira o limite superior de integração: '))

        lista_pontos = [x1]
        h = (x2 - x1) / n

        for i in range(1, n + 1):
            lista_pontos.append(x1 + i * h)

        return lista_pontos, h, x1, x2
    except:
        print('Algo deu errado!')
        exit(-1)


def func(x: float) -> float:
    return np.exp(x)


def create_graph(listax, listafx):
    x = [listax[0]]
    num = x[0] + 0.001
    while num <= listax[len(listax) - 1]:
        x.append(num)
        num += 0.001

    y = [func(i) for i in x]

    plt.plot(x, y, linestyle='dashed')

    for i in range(0, len(listafx) - 1):
        aux_x = [listax[i], listax[i + 1]]
        aux_y = [listafx[i], listafx[i + 1]]

        plt.plot(aux_x, aux_y)

        plt.plot([listax[i], listax[i]], [0, listafx[i]])

    plt.plot([listax[-1], listax[-1]], [0, listafx[-1]])

    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.title('Método do Trapézio Repetido')
    plt.show()


def integrate(listafx: list, h: float) -> float:
    aux = 0.0
    aux += listafx[0] + listafx[len(listafx) - 1] + 2 * sum(listafx[1:len(listafx) - 1])
    aux *= (h / 2.0)

    return aux


if __name__ == '__main__':
    lista_pontos, h, x1, x2 = setup()

    listafx = [func(i) for i in lista_pontos]
    resultado = integrate(listafx, h)

    print("O valor da integral da integral da função nos intervalos [%f,%f] é igual a "
          "%f" % (x1, x2, resultado))

    create_graph(lista_pontos, listafx)
