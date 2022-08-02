# faca um prog que leia um ano qualquer e mostre se ele e bissexto

year = int(input('Digite um ano: '))

# Dividir o valor por 4
# se o resto der 0 e bissexto, se der quebrado nao e bisexto

# O ANO E bissexto QUANDO E DIVISIVEL POR 4, MAS NAO POR 100
# se for divisivel por 100 e por 4 e preciso fazer mais um conta

# se for divisivel por 100 mas nao por 400, NAO É bissexto
# se for divisivel por 100 E POR 400, É bissexto


if year % 4 == 0:
    if year % 100 != 0:
        print('foi bissexto')
    else:
        if year % 400 != 0:
            print('Nao foi bissexto')
        else:
            print('Foi Bissexto')
else:
    print('Esse ano NAO foi bissexto')


# ou fazer assim

# ano = int(input('Que ano quer analisar?'))
# if ano % == 0 and ano % 100 != or ano % 400 == 0:
#   print(f'O ano {ano} é bissexto!')
#else:
#   print(f'O ano {ano} nao é bissexto')


