import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,3,7,10,13,16,18,21,25,28,31,33,34,37,40,42,45,49,51,56]) #esses serão os valores do eixo x
arquivo=open('magnitudes.txt') #abre o arquivo com os valores de luminosidade(magnitude)
dataVariavel=[] #array com os dados da luminosidade da estrela variável
dataStar1=[] #array com a luminosidade da estrela de referência 1
dataStar2=[] #'''''''''''''''''''''''' da estrela de referência 2
dataStar3=[] #'''''''''''''''''''''''' da estrela de referência 3

count=1 #variável auxiliar

for linhas in arquivo:
    linhas=linhas.strip() #retira o caractere \n no final da string

    if count < 21:
        dataVariavel.append(float(linhas))
    elif count < 41:
        dataStar1.append(float(linhas))
    elif count < 61:
        dataStar2.append(float(linhas))
    else:
        dataStar3.append(float(linhas))

    count+=1

plt.plot(x,dataVariavel,'go') #dados da estrela variavel como bolinhas verdes
plt.plot(x,dataVariavel,'b--',label='cefeiadas') #insere uma linha azul tracejada ligando as bolinhas

plt.plot(x,dataStar1,'ro') #dados da estrela de referência 1 como bolinhas vermelhas
plt.plot(x,dataStar1,'r--',label='referencia 1') #insere uma linha vermelha tracejada ligando as bolinhas

plt.plot(x,dataStar2,'bo') #dados da estrela de referência 2 como bolinhas azuis
plt.plot(x,dataStar2,'k--',label='referencia 2')#insere uma linha preta tracejada ligando as bolinhas

plt.plot(x,dataStar3,'yo')#dados da estrela de referência 3 como bolinhas amarelas
plt.plot(x,dataStar3,'g--',label='referencia 3')#insere uma linha tracejada verde ligando as bolinhas

plt.title("Magnitude X Dias")
plt.grid(True)

plt.xlabel("Dias")
plt.ylabel("Magnitude")

plt.show()
