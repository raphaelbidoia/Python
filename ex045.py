import random
from time import sleep
print('\033[47mVAMOS JOGAR!!!\033[m')
e = str(input('Escolha entre:'
              '\n\033[35mPedra\033[m'
              '\n\033[34mPapel\033[m'
              '\n\033[31mTesoura\033[m'
              '\nQual Você Vai Escolher?: '))
n1 = 'pedra'
n2 = 'papel'
n3 = 'tesoura'
l = [n1, n2, n3]
c = random.choice(l)
j = e.lower()
print('++'*20)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('++'*20)
if c == j:
    print(f'Empatamos'
          f'\nEu escolhi {c}'
          f'\nJogue novamente')
elif c == n2 and j == n1:
    print(f'Ganhei !!'
          f'\nEu escolhi {c}'
          f'\nJogue novamente')
elif c == n1 and j == n3:
    print(f'Ganhei !!'
          f'\nEu escolhi {c}'
          f'\nJogue novamente')
elif c == n3 and j == n2:
    print(f'Ganhei !!'
          f'\nEu escolhi {c}'
          f'\nJogue novamente')
elif c == n1 and j == n2:
    print(f'Perdi eu escolhi {c}'
          f'\nJogue novamente')
elif c == n3 and j == n1:
    print(f'Perdi eu escolhi {c}'
          f'\nJogue novamente')
elif c == n2 and j == n3:
    print(f'Perdi eu escolhi {c}'
          f'\nJogue novamente')
