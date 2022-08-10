# crie um prog que leia o ano de nascimento de 7 pessoas.
# no final, mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sao maiores
from datetime import date
maior = 0 
menor = 0
year = date.today().year #puxa o ano atual
for c in range (0, 7):
    ano = int(input('Digite o ano de nascimento: '))
    idade = year - ano
    if idade > 18:
        maior = maior + 1
    else:
        menor = menor + 1
print(f'{maior} Sao maiores de idade')
print(f'{menor} Sao menores de idade')
