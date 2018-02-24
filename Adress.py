enderecos = dict()
maximo=''

try:
    fhand=open(input('Insira o nome do arquivo: '))
    for linha in fhand:
        linha=linha.split()
        if linha[1] not in enderecos:
            enderecos[linha[1]]=1
        else:
            enderecos[linha[1]]+=1
except:
    print('Nome de arquivo inválido!')
    exit()

valores=[]
for chave in enderecos:
    valores.append(enderecos[chave])

for chave in enderecos:
    if enderecos[chave]==max(valores):
        maximo=chave

print('A pessoa que tem mais arquivos de email é %s com %d emails' % (maximo,enderecos[maximo]))
print(enderecos)
