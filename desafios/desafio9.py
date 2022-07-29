#num = 0
#while num <= 10:
#    i = 1
#    while i <= 10:
##        product = num*i
#        print(f'{num} * {i} = {product} \n')
#        i = i + 1
#       num = num + 1
#    print('\n')
#num = int(input('Multiplication using value? '))
#for i in range(1, num+1):
#    for j in range(1, num+1):
#        print(f'{i} * {j} = {i*j}')


num = int(input('Enter the number = '))
i = 1

while i<=10:
    print(f'{num} * {i:2} = {num*i}')
    i = i + 1
