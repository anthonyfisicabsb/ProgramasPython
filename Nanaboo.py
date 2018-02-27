filename=''
while filename!='na na boo':
	count=0
	filename=input('Enter file name: ')
	try:
		novoarquivo=open(filename)
		for linhas in novoarquivo:
			count+=1
		print(filename,'has',count,'subject lines')
	except:
		if filename!='na na boo':
			print('Nome de arquivo não encontrado!')
	if filename=='na na boo':
		print('NA NA BOO TO YOU!-You\'ve been punked')