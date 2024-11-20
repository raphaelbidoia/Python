numero=int(input('Digite um numero de 0 ate 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f'o numero digitado é:{numero}')
print('a Unidade é:{}'.format(u))
print('a Dezena é:{}'.format(d))
print('a Centena é:{}'.format(c))
print('o Milhar é:{}'.format(m))
