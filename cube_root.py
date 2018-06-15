guess = 0.0
num = float(input('insira um numero: '))
guess_number = 0

increase = 0.00001 if num > 0 else -0.00001
epsilon = 1e-4

print(increase)

while abs(num - guess**3) >= epsilon:
    guess_number += 1
    guess += increase

print('Numero de tentativas: ', guess_number)
print('Raiz de', num, 'eh', guess)
