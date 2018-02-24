name = input('Insira teu nome: ')

arquivo = open('guest.txt','w')

arquivo.write('%s é o nome de quem digitou' % name)
