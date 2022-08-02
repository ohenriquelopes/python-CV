# Escreva um programa que leia a vel de um carro.
# se ele ultrapassar 80Km, mostre uma msg dizendo que ele foi multado
# a multa vai custar 7 reais por cada km acima do limite


vel = int(input('Digite a velocidade do carro: '))

if vel > 80:
    print(f'Voce foi multado! O valor da multa será {(vel - 80) * 7}')
else:
    print('Voce nao foi multado')
