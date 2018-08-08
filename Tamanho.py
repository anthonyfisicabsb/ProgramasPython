maior=-99999999999999999999
menor=999999999999999999999
count=0
entrada=''
while entrada!='done':
	entrada=input('Insira o número aqui->')
	try:
		entrada=int(entrada)
		if entrada>= maior:
			maior=entrada
		if entrada<= menor:
			menor= entrada
		count+=1
	except:
		print('Invalid input')
		continue
if count>0:
	print('Maior->',maior)
	print('Menor->',menor)
else:
	print('Você não digitou nenhum número')