# crie um programa que faca o computador jogar jokenpo com voce

import random

print('''Escolha entre as opcoes:
[1] - Pedra
[2] - Papel
[3] - Tesoura''')

choice = int(input('Digite sua escolha: '))

num = random.randint(1,3)
print(num)

if (choice == 1 and num == 1): 
    print('Deu empate. Pedra e Pedra sao iguais')
elif (choice == 1 and num == 2):
    print('Voce perdeu. Pedra perde para papel')
elif (choice == 1 and num == 3):
    print('Voce ganhou. Pedra ganha de tesoura')
elif (choice == 2 and num == 1):
    print('Voce ganhou. Papel ganha de pedra')
elif (choice == 2 and num == 2):
    print('Deu empate. Papel e Papel sao iguais')
elif (choice == 2 and num == 3):
    print('Voce perdeu. Papel perde para tesoura')
elif (choice == 3 and num == 1):
    print('Voce perdeu. Tesoura perde para pedra')
elif (choice == 3 and num == 2):
    print('Voce ganhou. Tesoura ganha de papel')
elif (choice == 3 and num == 3):
    print('Deu empate. Tesoura e tesoura sao iguais')
