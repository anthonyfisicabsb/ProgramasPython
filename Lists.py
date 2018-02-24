def chop(lista):
    lista.pop(0)
    lista.pop(len(lista)-1)
    print(lista)
def middle(lista2):
    return lista2[1:len(lista2)-1]

novalista =[1,2,3,4,5,6,7,8,9]
print(middle(novalista))
chop(novalista)
