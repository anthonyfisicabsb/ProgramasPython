import numpy as np 
from scipy.optimize import curve_fit
import pylab as pl 
import csv

dadosx = list()
dadosy = list()

"""importando dados do comprimento e força"""
with open("dados.csv", "r") as arquivo:
	ler = csv.reader(arquivo, delimiter=",")

	for row in ler:
		dadosx.append(np.float64(row[0]))
		dadosy.append(np.float64(row[1]))


"""convertendo listas para um numpy_array"""
x_dados = np.array(dadosx)
y_dados = np.array(dadosy)

""" modelo esperado da equação a ser obtida na regressão"""
def func(x, A, B):
	return A / (x**B)

popt, pcov = curve_fit(func, x_dados, y_dados)
A, B = popt


yfitted = func(x_dados, A, B)

"""plotagem do gráfico"""
pl.title("Gráfico Força x Comprimento(Python 3.6.5)")
pl.scatter(x_dados, y_dados, c='red')
pl.plot(x_dados, yfitted, "-", label='f(x) = 2054.95*(x^-2.02)')
pl.xlabel("Comprimento (cm)")
pl.ylabel("Força (N)")
pl.legend()
pl.show()
