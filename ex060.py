'''s = 1
r = 1
print('digite um valor para saber seu fatorial: ')
n = int(input('Digite o numero: '))
while r <= n:
    s *= r
    r += 1
print(s)

# r = contador
# s = resultado
# n = numero
médodo 
:::escrita para entender::: 
resultado = 1
contador = 1 
numero = escreva um numero para saber o fatorial
numero 
enquanto contador < = numero
    resultado = resultado * contador
    contador = contador + 1
resposta do fatorial
from math import factorial
n = int(input('para saber o fatorial, digite um numero: '))
f = factorial(n)
print(f'o fatorial de {n} é {f}')'''
n = int(input('para saber o fatorial, digite um numero: '))
c = n
f = 1
while c > 0:
    print(c, end='')
    print(' X ' if c > 1 else ' =', end='')
    f *= c
    c -= 1
print(f' {f}')
