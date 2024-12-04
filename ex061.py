n = int(input('Primeiro termo: '))
n2 = int(input('Razão: '))
t = n
c = 1
while c <= 10:
    print(t, end='-> ')
    t += n2
    c += 1
print('Acabou')
