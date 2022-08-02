# leia o nome de uma cidade e diga se ela comeca ou nao com o nome "santo"


c = input('Digite o nome de uma cidade: ').strip()
a = c.lower()
t = a.find('santo')
if t == 0:
    print(f'Ela comeca com santo')
else:
    print(f'Ela nao comeca com santo')


