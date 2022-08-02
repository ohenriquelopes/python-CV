# desenvolta um progm que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo


r1 = int(input('Digite o valor da reta 1: '))
r2 = int(input('Digite o valor da reta 2: '))
r3 = int(input('Digite o valor da reta 3: '))


#|r1 - r3 | < r2 < r1 + r3

x = abs(r1 - r3) < r2 < (r1 + r3)

if (x == True):
    print('É possivel formar um triangulo')
else:
    print('Nao é possivel formar um triangulo')
