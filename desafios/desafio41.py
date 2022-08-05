# um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade
# ate 9 anos mirim
# ate 14 infantil
# ate 19 junior
# ate 20 senior
# acima master

from datetime import date 

cy = date.today().year #importa somente o ano atual

year = int(input('Digite o seu ano de nascimento: '))

if (cy - year <= 9):
    print('Sua categoria é Mirim')
elif (cy - year <= 14):
    print('Sua categoria é Infantil')
elif (cy - year <= 19):
    print('Sua categoria é Junior')
elif (cy - year <= 20):
    print('Sua categoria é Senior')
else:
    print('Sua categoria é Master')
