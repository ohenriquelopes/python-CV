#refaca o desafio 009 mostrando a tabuada de 1 numero que o usuario escolher so que usando o laco FOR

n = int(input('Digite o numero da sua tabuada: '))
i = 0
for t in range(0, 11):
    print(f'{n} x {i} = {n * i}')
    i = i + 1
