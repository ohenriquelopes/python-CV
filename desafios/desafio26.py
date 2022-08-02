# leia uma frase e mostre
# quantas vezes aparece a letra "a"
# em que posicao ela aparece pela primera vez
# em que posicao ela aparece a ultima vez


g = input('Digite uma frase para saber quantas letras A aparecem: '.lower())

a = g.count('a')
ind = g.find('a')
last = g.rfind('a') 
print(f'A letra A aparece {a} vezes')
print(f'A posicao da letra A na primeira vez é {ind}')
print(f'A ultima posicao da letra A é {last}')

