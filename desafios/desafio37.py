# um programa que leia um numero inteiro qualquer e peca para o usuario escolher qual sera a base de conversao
# 1 para binario, 2 para octal e 3 para hexadecimal

num = int(input('Digite um numero inteiro: '))

choice = int(input('''
Digite 1 para converter para binario
Digite 2 para converter para octal
Digite 3 para converter para hexadecimal
Escolha: '''))


if (choice == 1):
    binary = bin(num).replace("0b", "")
    print(f'{num} em binario é {binary}')
elif (choice == 2):
    octal = oct(num).replace("0o","")
    print(f'{num} em octal é {octal}')
else: 
    hexa = hex(num).replace("0x","").upper()
    print(f'{num} em hexadecimal é {hexa}')

# ou deixar 
# print(" as opcoes 1,2,3")
# opcao = int(input('Sua opcao: '))
# if opcao == 1: .....
# print(f'{num} convertido para binario é igual a {num, bin(num)[2:]}')
