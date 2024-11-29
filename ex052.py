'''n = int(input('Digite um numero:'))
def is_prime(n):
    if n < 2:
        return False
    for c in range(2, int(n ** 0.5) + 1):
        if n % c == 0:
            return False
    return True
if is_prime(n):
    print('numero primo')
else:
    print('não é um numero primo')'''

n = int(input('Digite um numero: '))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        t += 1
    else:
        print('\033[30m', end=' ')
    print(c, end=' ')
print(f'\n\033[mO numero {n} foi dividido {t} vezes')
if t ==2:
    print('Ele é primo')
else:
    print('Ele não é primo')
