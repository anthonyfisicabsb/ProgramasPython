def computpagamento(hrs,val):
	salarioBruto=0.0
	if (hrs-40)>0:
		adicional= (hrs-40)*(1.5*val)
		salarioBruto=(40*val)+adicional
	else:
		salarioBruto=horasTrabalhadas*valorHora
	return salarioBruto
	
try:
	horasTrabalhadas = int(input('Horas trabalhadas: '))
	valorHora = float(input('Valor/hora: '))
	salarioBruto= computpagamento(horasTrabalhadas,valorHora)
	print('Salario bruto:',round(salarioBruto,2))
except:
	print('Você inseriu algum valor não numérico no valor da hora ou nas horas trabalhadas')