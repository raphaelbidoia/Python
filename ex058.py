'''import random
from time import sleep
c = 0
n1 = random.randint(0, 10)
print('-=-'*20)
print('Escolha um numero para ganhar um prêmio!')
print('-=-'*20)
n2 = (int(input('digite um numero de 0 ate 10: ')))
print('processando...')
while n1 != n2:
    print('eu ganhei tente novamente!')
    n2 = (int(input('digite um numero de 0 ate 10: ')))
    print('processando...')
    sleep(1)
    c += 1
if n1 == n2:
    print('-=-' * 20)
    print(f'VOCÊ É O GRANDE VENCEDOR voce precisou de {c} tentativas')'''
#professor
from random import randint
computer = randint(0, 10)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('qual seu palpite? '))
    palpite+=1
    if jogador == computer:
        acertou = True
    else:
        if jogador < computer:
            print('Mais... tente novamente')
        elif jogador > computer:
            print('Menos... tente novamente')
print(f'Acertou com {palpite} tentativas. Parabens!')
