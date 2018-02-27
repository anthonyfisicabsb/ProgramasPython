numeros=[1,2,3]
nomes= ['alberto','carlos','simone']
misto= [1,2,3.0,'alberto','carlos',3.5,'simone']
listas=[numeros,nomes,misto]
print listas
print len(numeros)
print numeros[-1] #pega o último valor do vetor
vetor2 = misto[3:] #pegar uma fatia da lista e colocar em outra
print vetor2
misto.sort()
print misto
misto.reverse()
print misto
numeros2 = [4,5,6]
numeros.extend(numeros2)
print numeros
input()