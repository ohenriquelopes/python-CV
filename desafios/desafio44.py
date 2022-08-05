# elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preco normal e condicao de pagamento

# a vista dinheiro/cheque 10% desconto
# a vista no cartao 5% desconto
# em ate 2x no cartao preco normal
# 3x ou mais no cartao 20% de juros

valor = float(input('Digite o valor do produto: '))

print(''' Qual será a forma de pagamento?
[1] - A vista dinheiro/cheque 10% desconto
[2] - A vista no cartao 5% desconto
[3] - Em até 2x no cartao sem desconto
[4] - 3x ou mais no cartao 20% de JUROS''')
choice = int(input('Digite a opcao de pagamento: '))

if choice == 1:
    print(f'O valor do seu produto será {valor * 0.9}')
elif choice == 2:
    print(f'O valor do seu produto será {valor * 0.95}')
elif choice == 3:
    print(f'O valor do seu produto será {valor}')
elif choice == 4:
    print(f'O valor do seu produto será {valor * 1.2}')

