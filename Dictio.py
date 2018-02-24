dictio=dict()

try:
    arquivo=open('words.txt')
    for linhas in arquivo:
        linhas=linhas.strip()
        dictio.__setitem__(linhas,2)
except:
    print('Arquivo não encontrado')
sea=input('Digite o nome de uma chave: ')
print(sea in dictio)
print(dictio)
