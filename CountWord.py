def count(palavra,letra):
	count=0
	for letras in palavra:
		if letras == letra:
			count+=1
	print('A letra apareceu',count,'vezes na palavra')
	
entrada=input('Insira um string-> ')
cara=input('Insira o caractere prourado-> ')
if len(cara)>1:
	print('Insira apenas um caractere')
else:
	count(entrada,cara)