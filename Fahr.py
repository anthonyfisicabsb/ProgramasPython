try:
	celsius= float(input('Insira a temperatura em Celsius: '))
	fahr = ((celsius*9.0)/5.0) + 32
	print('A temperatura convertida para Fahrenheit é',round(fahr,2))
except:
	print('Você não inseriu um número!')