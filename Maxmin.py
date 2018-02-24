entrada=''
listaDeNumeros=[]

while True:
    try:
        entrada=input('Insira um número: ')
        if entrada=='pronto':
            break
        entrada=float(entrada)
        listaDeNumeros.append(entrada)
    except:
        print('O valor digitado não é um número!')
print('O maior número é %f' % max(listaDeNumeros))
print('O menor número é %f' % min(listaDeNumeros))
print(listaDeNumeros)
