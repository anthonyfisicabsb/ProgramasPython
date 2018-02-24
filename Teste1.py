def teste1(nome,**numeros):
    print(nome + ":")
    for i in numeros.keys():
        print('%10s : %d' % (i,numeros[i]))

def teste2(nome,*strings,**numeros):
    print(nome + ":")
    for i in strings:
        print('> ',i)
    keys=[]
    for chave in numeros:
        keys.append(chave)
    keys.sort()
    for i in keys:
        print('%10s : %d' % (i,numeros[i]))

teste1('Numeros',um=1,dois=2,tres=3,quatro=4,cinco=5)
teste2('Numeros','Os numeros são ordenados','pelos seus nomes',um=1,dois=2,tres=3,quatro=4,cinco=5)
