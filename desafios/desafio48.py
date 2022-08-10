# faca um prog que calcule a soma entre todos os numeros impares que sao multiplos de 3 e que se encontram no intervalo de 1 ate 500

sum = 0
cont = 0
for s in range(0, 500):
    if s % 2 == 1 and s % 3 == 0: # verifica se o numero é impar (s % 2 == 1) Verifica se ele e multiplo de 3 (s % 3 == 0)
        cont = cont + 1
        sum = sum + s # faz a soma em toda a iteracao
print(sum)
