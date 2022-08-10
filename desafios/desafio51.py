# dev um prog que leia o primeiro termo e a razao de uma PA. No final, mostre os 10 primeiros termos dessa progressao


p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razao da PA: '))

for pa in range(0, 10):
    print(p)
    p = p + r
