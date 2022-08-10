# dev um progm que leia o NOME, IDADE, SEXo de 4 pessoas. Mostre no final
# a media de idade do grupo
# qual e o nome do homem mais velho
# quantas mulhertes tem menos de 20 anos
name = []
media = 0
sidade = 0
for p in range(0, 4):
    name = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: '))
    print("    ")
    sidade = sidade + idade
 

media = sidade / 4
print(name)
print(f'A media da idade do grupo é {media}')
