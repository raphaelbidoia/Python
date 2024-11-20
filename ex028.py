import random
from time import sleep
n1 = random.randint(0, 5)
print('-=-'*20)
print('Escolha um numero para ganhar um prêmio!')
print('-=-'*20)
n2 = (int(input('digite um numero de 0 ate 5: ')))
print('processando...')
sleep(3)
if n1 == n2:
    print('VOCÊ É O GRANDE VENCEDOR')
else:
    print(f'Tente novamente! o numero do sorteio foi: {n1}')
