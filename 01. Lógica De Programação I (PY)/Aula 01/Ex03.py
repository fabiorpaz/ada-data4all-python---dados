"""
3. Crie um programa que leia dois números e printe na tela os valores das operações apos a descrição da operacao ex:
a = 10
b = 15
Adicao: 10 + 15 = 25
Subtracao: 10 - 15 = -5
Multiplicaca: 10 * 15 = 150              
Resto modular: 10 % 15 = 10
"""
x = int(input('Informe o valor de x: '))
y = int(input('Informe o valor de y: '))

print (f'Adicao: {x} + {y} = {x + y}\nSubtracao: {x} - {y} = {x - y}\nMultiplicacao: {x} * {y} = {x * y}\nResto modular: {x} % {y} = {x % y}')