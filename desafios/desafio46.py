# mostre na tela uma contagem regressiva para o estouro de fogos de artifico. Indo de 10 até 0. com pausa de 1 seg entre eles

import time
for c in range(10, -1, -1):
    time.sleep(1)
    print(c)
