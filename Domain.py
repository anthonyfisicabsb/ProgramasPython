dominios=dict()

try:
    fhand=open(input('Insira o nome do arquivo: '))

    for linha in fhand:
        if linha.startswith('From'):
            linha=linha.split()
            linha=linha[1]
            linha=linha[linha.find('@'):]

            if linha not in dominios:
                dominios[linha]=1
            else:
                dominios[linha]+=1
except:
    print('Arquivo não encontrado!')

print(dominios)
