# crie um progrm que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final
# de acordo com a media atingida
# media abaixo de 5 reprovado
# media entre 5 e 6.9 recuperacao
# media 7 ou superior aprovado

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1 + n2) / 2
print(media)
if (media < 5):
    print('REPROVADO')
elif (media >= 7):
    print('APROVADO')
else:
    print('RECUPERACAO')
