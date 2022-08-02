# leia o nome completo de uma pessoa mostrando em seguida o primeiro e o ultimo nome separadamente
# ex ana maria de souza
# primeiro = ana
#ultimo = souza


name = str(input('Digite seu nome completo: '))

sname = name.split()
print(f'Primeiro = {sname[0]}')
print(f'Ultimo = {sname[-1]}')
