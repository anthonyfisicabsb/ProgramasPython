filename=input('Enter file name: ')
aux=True
while aux:
	try:
		novoarquivo=open(filename)
		aux=False
	except:
		print('Nome de arquivo não encontrado!')
		filename=input('Enter file name: ')
	
for linhas in novoarquivo:
	linhas=linhas.rstrip()
	print(linhas.upper())
novoarquivo.close()