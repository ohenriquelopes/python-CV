# Leia o comprimento do cateto oposto e do adjacente de calcule e mostre a hipotenusa
import math
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))

print(f'A hipotenusa é {math.hypot(co, ca)}')
