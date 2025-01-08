valor = int(input('Digite o valor a ser sacado R$: '))
total = valor
c = 50
tc = 0
while True:
    if total >= c:
        total -= c
        tc += 1
    else:
        if tc > 0:
            print(f'Total de {tc} Cédulas de R$ {c}')
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        tc = 0
        if total == 0:
            break
