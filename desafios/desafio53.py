# crie um programa que leia uma frase qualquer e diga se ela e um palindromo
# desconsiderando os espacos

frase = str(input('Digite uma frase qualquer para descobrir se e um palindromo: '))

f1 = frase.replace(' ', '').lower()

if f1 == f1[::-1]:
    print('Essa frase é um palindromo')
else:
    print('Essa frase não é um palindromo')
    
