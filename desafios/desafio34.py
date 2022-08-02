# Escreva um progrm que pergunte o salario de um funcionario e calcule o valor do seu aumento
# para salarios superiores a 1250, calcule um aumento de 10%
# para os salarios inferiores ou iguais, o aumento é de 15%

sal = float(input('Digite o valor do seu salario: '))

if (sal <= 1250):
    print('15%')
    print(f'O valor do seu novo salario é {sal * 1.15:.2f}')
else:
    print('10%')
    print(f'O valor do seu novo salario é {sal * 1.10:.2f}')
