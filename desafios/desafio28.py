# faca o computador pensar em um numero inteiro entre 0 e 5 e peca para o usuario
# tentar descobrir qual foi o numero escolhido pelo computador
# O programa devera escrever se o usuario venceu ou perdeu

import random

m = random.randint(0, 5)
print(m)
choice = int(input('Adivinhe o numero entre 0 e 5: '))

if choice == m:
    print(f'Parabens! Voce adivinhou o numero!')
else:
    print(f'Voce errou. Tente novamente!')
