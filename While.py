x=0
count=0
entrada=''
while entrada!='done':
	entrada=input('Insira o número aqui->')
	try:
		entrada=int(entrada)
		x+=entrada
		count+=1
	except:
		print('Invalid input')
		continue
if count>0:
	print(x,count,float(x)/count)
else:
	print(0,0,0.0)
