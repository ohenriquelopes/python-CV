# um prof quer sortear um dos seus quatro alunos para apagar o quadro. O programa  deve ler o nome e escrever o nome do escolhido
import random
n1 = input('Digite o nome do aluno 1: ')
n2 = input('Digite o nome do aluno 2: ')
n3 = input('Digite o nome do aluno 3: ')
n4 = input('Digite o nome do aluno 4: ')

num = random.randint(1,4)

if num == 1:
    print(f'O aluno é {n1}')
elif (num == 2):
    print(f'O aluno é {n2}')
elif (num == 3):
     print(f'O aluno é {n3}')
else:
    print(f'O aluno é {n4}') 
    
    
    
    

