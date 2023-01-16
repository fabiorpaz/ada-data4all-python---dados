# Ex1: Checar se dado número no input é positivo, negativo ou igual a 0.

a = float(input('Informe o numero a ser analisado: '))

if a == 0:
    print ('O numero escolhido foi 0')
elif a > 0:
    print('O numero escolhido é positivo.')
else:
    print('O numero escolhido é negativo.')