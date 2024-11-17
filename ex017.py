''' n1=float(input('digite o valor do cateto oposto: '))
n2=float(input('o valor do cateto adjacente: '))
h=n1**2+n2**2
h1=h**(1/2)
print('O valor da hipotenusa é {:.2f}'.format(h1)) '''
'''import math
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento co cateto adjacente: '))
h1 = math.hypot(co, ca)
print('o valor da Hipotenusa é de: {:.2f}'.format(h1))'''
from math import hypot
co = float(input('valor do cateto oposto: '))
ca = float(input('valor do cateto adjacente'))
h1=hypot(co, ca)
print('o valor da hipotenusa é de {:.2f}'.format(h1))
