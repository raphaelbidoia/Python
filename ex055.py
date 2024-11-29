cont = 0
cont1 = 0
for c in range(1, 6):
    n = float(input(f'digite o peso da {c}º pessoa em kg: '))
    if c == 1:
        cont = n
        cont1 = n
    else:
        if n > cont:
            cont = n
        if n < cont1:
            cont1 = n
print(f'o maior peso foi de {cont}KG e o menor peso foi de {cont1}KG')
