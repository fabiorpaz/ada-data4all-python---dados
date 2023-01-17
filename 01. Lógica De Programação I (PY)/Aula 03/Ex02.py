# Ex2. Contar o numero de vogais de uma palavra lida pelo input(). Ex: apple => 2
palavra = input('Insira a palavra: ')
vogais = 0
cont = len(palavra) - 1
while cont >= 0:
    if palavra[cont].lower() in 'aeiou':
        vogais += 1
    cont -= 1
print (vogais)