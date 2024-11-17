'''import math
n0=int(input('coloque um angulo pra que descubra os valores de seno cosseno e tangente: '))
n=math.sin(math.radians(n0))
n1=math.cos(math.radians(n0))
n3=math.tan(math.radians(n0))
print(f'os valores são\n'
      f'seno: {n}\n'
      f'cosseno: {n1}\n'
      f'tangente: {n3}')'''
import math
n0=int(input('coloque um angulo pra que descubra os valores \n'
             'de seno, cosseno e tangente: '))

n1=math.cos(math.radians(n0))
n2=math.sin(math.radians(n0))
n3=math.tan(math.radians(n0))

print('os valores para o angulo {} colocado é:\n'
      'cosseno: {:.2f}\n'
      'seno: {:.2f}\n'
      'tangente: {:.2f}'.format(n0, n1, n2, n3))
