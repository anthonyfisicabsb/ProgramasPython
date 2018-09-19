import matplotlib.pyplot as plt

numeros = ['II', 'II', 'SR', 'SR', 'MI', 'MI', 'MI', 'MI', 'MM', 'MM', 'MM',
           'MM', 'MS','MS', 'SS']

plt.hist(numeros)
plt.title('Histograma de Notas Finais')
plt.ylabel('Frequencia de notas')
plt.xlabel('Mencoes')
plt.plot()
plt.show()
