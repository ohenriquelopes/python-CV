# um programa que pergunte a distancia de uma viagem em km.
# Calcule o preco da passagem, cobrando 0,50 por km para viagens ate 200km 
# e 0,45 para viagens mais longas

dist = int(input('Digite a distancia da sua viagem: '))

if (dist <= 200):
    print(f'O valor da sua passagem é {dist * 0.5}')
else:
    print(f'O valor da sua passagem é {dist * 0.45}')

