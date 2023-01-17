"""
Ex4: Ler o CPF da pessoa (apenas numeros ex: 99988877766) e formatar no tipo XXX.XXX.XXX-XX
obs: Se o CPF tiver menos de 11 digitos, preencher com zeros, ex: 005.923.432-01
Dica: .zfill() e len()
"""
cpf = input('Digite os numero do CPF: ')

if len(cpf) < 11:   # len() registra a quantidade de caracteres
    cpf = cpf.zfill(11) # .zfill() preenche o escopo escolhido com "0"

print (f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}')
