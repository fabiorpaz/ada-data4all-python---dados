# 6. Crie um programa que calcule a media ponderada de 3 valores obtidos pelo input() com seus respectivos pesos(p1, p2 e p3)

valor1 = float(input('Digite o primeiro valor: '))
p1 = int(input('Digite o peso do primeiro valor fornecido: '))
valor2 = float(input('Digite o segundo valor: '))
p2 = int(input('Digite o peso do segundo valor fornecido: '))
valor3 = float(input('Digite o terceiro valor: '))
p3 = int(input('Digite o peso do terceiro valor fornecido: '))

print(f'A media ponderado dos valores fornecidos é: {(valor1*p1+valor2*p2+valor3*p3)/(p1*p2*p3)}')