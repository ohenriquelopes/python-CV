# um programa que leia dois numeros inteiros e compare-os, mostrando uma mensagem na tela
# O primeiro valor e maior
# O segundo valor e maior
# Nao existe valor maior, os dois sao iguais

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

if (num1 > num2):
    print('O primeiro numero é maior')
elif (num2 > num1):
    print('O segundo numero é maior')
elif (num1 == num2): # () sao opcionais nesse caso
    print('Não existe numero maior, os dois são iguais')
