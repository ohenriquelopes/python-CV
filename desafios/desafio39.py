# um programa que leia o ano de nascimento de um jovem e informe, de acorcom sua idade
# se ele ainda vai se alistar ao servico militar
# se e a hora de se alistar
# se ja passou do tempo do alistamento
# o programa tbm devera mostrar o tempo que falta ou que passou do prazo

from datetime import date
y = int(input('Digite seu ano de nascimento: '))

year = date.today().year #importa somente o ano atual

if (year - y > 19):
   print('Já passou o seu tempo de alistamento') 
elif (year - y == 18):
    print('Voce deve ir se alistar')
else:
    print('Nao chegou a hora do seu alistamento, ainda')
