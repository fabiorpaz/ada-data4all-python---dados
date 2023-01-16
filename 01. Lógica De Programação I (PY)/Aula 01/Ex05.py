# 5. Crie um programa para calcular o valor da formula de bhaskara usando o input().

a = int(input('Informe o valor de a: '))
b = int(input('Informe o valor de b: '))
c = int(input('Informe o valor de c: '))

delta = (b ** 2) - 4 * a * c

if a == 0:
    print("O valor de a não deve ser 0")
elif delta < 0:
    print("Sem raízes reais")
else:
    x1 = (-b + delta ** 0.5) / (2 * a) # ou **(1/2) como expoente para raiz
    x2 = (-b - delta ** 0.5) / (2 * a)
    print (f'O valor da formula de bhaskara é:\nx1:{x1}\nx2:{x2}')