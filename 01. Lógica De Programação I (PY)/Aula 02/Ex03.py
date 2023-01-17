""" 
Ex3: A partir de um valor(salario) no input(ex: 3560.80), calcular o imposto de renda seguindo as faixas abaixo.
Printar na tela no formato R$1,000.00
faixa_1 = (salario < 1900) # isento
faixa_2 = (salario => 1900 and salario < 2826) # 7.5% salario
faixa_3 = (salario >= 2826 and salario < 3750) # 15% salario
faixa_4 = (salario >= 3750) # 22.5% do salario
"""
salario = float(input('Digite o salario: '))

if salario < 1990:
    imposto = 'isento'
elif salario < 2826:
    imposto = (f'no valor de R${salario*0.075:,.2f}') #0.075 é a porcentagem do valor de imposto
elif salario < 3750:
    imposto = (f'no valor de R${salario*0.15:,.2f}')
else:
    imposto = (f'no valor de R${salario*0,225:,.2f}')

print (f'O valor de imposto de renda será {imposto}')