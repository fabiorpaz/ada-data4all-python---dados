"""
2. Expressar o valor da formula de bhaskara: (-b + sqrt(b^2 - 4ac)) / 2*a
dado a = 2, b = 10 e c = 5 (receber essas variaveis via teclado)
"""
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
    print (f'x1:{x1}\nx2:{x2}')
""" 
2.1 Criar uma variavel `is_positive` booleana, com o valor True ou False usando um operador (">", "<") e a variavel
do valor calculado, que checa se o valor calculado é positivo.
"""
print (f'este valor é positivo? {delta>0}')

