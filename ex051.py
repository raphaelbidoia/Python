n = int(input('Primeiro termo: '))
n2 = int(input('Razão: '))
d = n + (10 - 1) * n2
for c in range(n, d + n2, n2):
    print(c, end=' -> ')
print('acabou')
