# leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
#ex digite um numero: 1834
# unidade: 4 dezena: 3 centena: 8 milhar: 1

n = int(input('Digite um numero de 0 a 9999: '))
# result = [int(a) for a in str(n)]

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print(f'Milhar {m}')
print(f'Centena: {c}')
print(f'Dezena: {d}')
print(f'Unidade: {u}')


