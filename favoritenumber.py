import json

try:
    filename= open('nomeusuario.json','r')
    
    nome = json.load(filename)

    print("Welcome back %s" % nome)

except FileNotFoundError:
    filename= open('nomeusuario.json','w')

    nome = input('Insira o teu nome: ')

    json.dump(nome,filename)

    print('Lembrarei do teu nome quando retornar',nome)
