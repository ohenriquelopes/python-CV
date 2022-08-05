# Escreva um prog para aprovar o emprest para a compra de 1 casa
#O prog vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar
# calcule o valor da prestacao mensal, sabendo que ela nao pode exceder 30% do salario ou entao o emprest sera negado

casa = float(input(f'Qual o valor da casa? '))
sal = float(input(f'Qual valor do seu salario? '))
anos = int(input('Em quantos anos voce vai pagar? '))

meses = anos * 12

emprestimo = sal / 0.3

parcela = casa / meses


if (parcela > emprestimo):
    print('O seu emprestimo nao foi aprovado')
else:
    print(f'Parabens! Seu emprestimo foi aprovado. O valor mensal da parcela é {parcela:.2f}')

