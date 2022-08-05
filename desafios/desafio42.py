# refaca o desafio 35 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado
# equilatero todos os lados iguais
# isosceles dois lados iguais
# escaleno todos os lados diferentes


r1 = int(input('Digite o valor da reta 1: '))
r2 = int(input('Digite o valor da reta 2: '))
r3 = int(input('Digite o valor da reta 3: '))


#|r1 - r3 | < r2 < r1 + r3

x = abs(r1 - r3) < r2 < (r1 + r3)

if (x == True):
    print('É possivel formar um triangulo')
    if (r1 == r2 == r3):
        print(f'Esse é um triangulo equilatero')
    elif (r1 == r2 or r1 == r3):
        print('Esse é um triangulo isosceles')
    else:
        print('Esse é um triangulo escaleno')
else:
    print('Nao é possivel formar um triangulo')



