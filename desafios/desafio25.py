# leia o nome de uma pessoa e diga se ela tem "silva" no nome

p = input('Digite o nome completo de uma pessoa: ')
l = p.lower()
f = l.find('silva')
if f == -1:
    print('Ela nao tem silva no nome')
else:
    print('Ela tem silva no nome')

