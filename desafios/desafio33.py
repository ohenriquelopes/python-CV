# faca um programa que leia tres numeros e mostre qual e o maior e qual e o menor


l = []

while len(l) < 3:
    x = int(input('Escreva um numero: '))
    l.append(x)
#print(l)

max_value = max(l)
print(f'O maior valor é {max_value}')

min_value = min(l)
print(f'O menor valor é {min_value}')
