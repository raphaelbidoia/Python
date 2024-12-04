n = int(input('Primeiro termo: '))
n2 = int(input('Razão: '))
t = n
c = 1
total = 0
n3 = 10
while n3 != 0:
    total += n3
    while c <= total:
        print(t, end='-> ')
        t += n2
        c += 1
    print('pausa')
    n3 = int(input('\nquantos termos vc quer mostrar a mais?'))
print(f'a função foi finalizada com {total} segmentos')


