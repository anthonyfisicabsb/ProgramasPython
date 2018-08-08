def compgrau(pt):
	if pt>= 0.9:
		return 'A'
	elif pt>= 0.8:
		return 'B'
	elif pt>= 0.7:
		return 'C'
	elif pt>= 0.6:
		return 'D'
	else:
		return 'F'
		
try:
	num=float(input('Insira um número entre 0.0 e 1.0: '))
	if num>=0.0 and num<=1.0:
		print(compgrau(num))
	else:
		print('O valor encontra-se fora do intervalo definido')
except:
	print('Erro! Insira um número')
	
			