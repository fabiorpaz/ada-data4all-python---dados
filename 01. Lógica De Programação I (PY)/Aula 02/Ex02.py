# Ex2: Crie um programa para remover o caracter n-gésimo caracter de uma string(ex: 1th, 2th caracter)
frase = input ('Digite a frase: ')
posicao = int(input('Digite a posicao do caracter que deseja excluir: '))

print (f'A frase resultante de {frase}, removendo seu {posicao} caractere, é {frase[:posicao-1]+frase[posicao:]}')


