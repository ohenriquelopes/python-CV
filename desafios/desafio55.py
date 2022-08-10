# faca um prog que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos

p = []

for peso in range(0, 5):
    p1 = float(input('Digite o peso: '))
    p.append(p1)

print(max(p))
print(min(p))
