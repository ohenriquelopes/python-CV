#  leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente
import math
n = float(input('Digite o valor de um angulo: '))
#print(f'O valor de seno de {n} é {math.sin(n)} o cosseno é {math.cos(n)} e a tangente é {math.tan(n)}')
sen = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tan = math.tan(math.radians(n))

print(f'O angulo de {n} tem o seno de {sen:.2f} o cosseno de {cos:.2f} e a tangente de {tan:.2f}')
