name=''
arquivo = open('guest_book.txt','a')

while name != 'none':
    name=input('Insira seu nome: ');

    if name != 'none':
        print('%s acabou de entrar' %name)
        arquivo.write('%s acabou de entrar\n' % name)
