import matplotlib.pyplot as plt
import re  # regex library
import math
import numpy as np

lim = 0.00001  # tamanho da constante h

"""Função para plotar gráfico no matplotlib"""


def create_graph(x, y, y2, y3, y4):
    plt.ylabel('y')
    plt.xlabel('x')
    plt.plot(x, y)  # diferenciação progressiva
    plt.plot(x, y2)  # diferenciação finita central
    plt.plot(x, y3)  # segunda derivada
    plt.plot(x, y4, linestyle='dashed')  # função original
    plt.title('Derivacao Numerica')
    plt.legend(['diff_progr', 'diff_central', '2deriv', 'original'])
    plt.grid()
    plt.show()


"""Método para ler arquivo e criar função de modo dinâmico"""


def read_file(x):
    retorno = 0.0
    with open('funcoes.txt') as arquivo:
        for line in arquivo:
            if re.match('(-?\d)P(-?\d)', line) != None:
                aux = re.match('(-?\d)P(-?\d)', line)
                const1 = int(aux.group(1))
                exp = int(aux.group(2))
                retorno += const1 * (x**exp)
            elif re.match('(-?\d)log(/d)', line) != None:
                aux = re.match('log(\d)', line)
                const = int(aux.group(1))
                base = int(aux.group(2))
                retorno += const * math.log(x, base)
            elif re.match('(-?\d)ln', line) != None:
                aux = re.match('(-?\d)ln', line)
                const = int(aux.group(1))
                retorno += const*math.log(x)
            elif re.match('(-?\d)exp(-?\d)', line) != None:
                aux = re.match('(-?\d)exp(-?\d)', line)
                const = int(aux.group(1))
                const2 = int(aux.group(2))
                retorno += const*math.exp(const2*x)
            elif re.match('(-?\d)sin(\d)', line) != None:
                aux = re.match('(-?\d)sin(\d)', line)
                A = int(aux.group(1))
                B = int(aux.group(2))
                retorno += A * np.sin(B*x)
            elif re.match('(-?\d)cos(\d)', line) != None:
                aux = re.match('(-?\d)cos(\d)', line)
                A = int(aux.group(1))
                B = int(aux.group(2))
                retorno += A * np.cos(B*x)
            elif re.match('(-?\d)sqrt', line) != None:
                aux = re.match('(-?\d)sqrt', line)
                A = int(aux.group(1))
                retorno += A * math.sqrt(x)
            elif re.match('(-?\d)sinh(\d)', line) != None:
                aux = re.match('(-?\d)sinh(\d)', line)
                A = int(aux.group(1))
                B = int(aux.group(2))
                retorno += A * np.sinh(B*x)
            elif re.match('(-?\d)cosh(\d)', line) != None:
                aux = re.match('(-?\d)cosh(\d)', line)
                A = int(aux.group(1))
                B = int(aux.group(2))
                retorno += A * np.cosh(B*x)

    return retorno


def funcao(x):
    return read_file(x)


"""Método para criar uma lista com os resultados da função original"""


def lista_funcao(x):
    y_list = []

    for num in x:
        y_list.append(funcao(num))

    return y_list


"""Método para encontrar derivada a partir da diferença progressiva"""


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


"""Método para encontrar derivada a partir da diferença central finita"""


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


"""Método para encontrar segunda derivada"""


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
    x_list = []  # domínio da função

    numero = 0.1  # número inicial
    while numero <= 5.0:
        x_list.append(numero)
        numero += 0.001

    finite_diff = finiteDif(x_list)
    finite_cent_diff = finitecCentralDif(x_list)
    sec_diff = secondDif(x_list)
    func_origin = lista_funcao(x_list)

    create_graph(x_list, , finite_diff, finite_cent_diff, sec_diff, func_origin)
