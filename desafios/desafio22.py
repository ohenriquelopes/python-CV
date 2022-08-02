#Leia o nome completo de uma pessoa e mostre 
# o nome com todas as letras maiusculas
# o nome com todas minusculas
# quantas letras ao todo (sem considerar espacos)
#Quantas letras tem o primeiro nome

name = str(input('Digite seu nome completo: '))
f_name = name.split()
comp = len(''.join(f_name))
print(f'Nome com todas maiusculas {name.upper()}')
print(f'Nome com todas minusculas {name.lower()}')
print(f'O seu nome tem {comp} letras')
# print(f'Seu nome tem ao todo {len(name) - name.count(' ')}')
print(f'O seu primeiro nome tem {len(f_name[0])} letras')
# print(f'Seu primeiro nome tem {name.find(' ')}')



