cont = 0
cont1 = 0
velho = 0
nomevelho = ''
for c in range(1, 5):
    print('----'*4)
    n = str(input('Nome: ')).strip()
    s = int(input('Sexo feminino 1\nmasculino 2 \n[1 / 2]: '))
    i = int(input('Idade: '))
    cont1 += i
    if c == 1 and s == 2:
        velho = i
        nomevelho = n
    if s == 2 and i > velho:
        velho = i
        nomevelho = n
    if s == 1 and i < 20:
        cont += 1
print(f'O nome do homem mais velho é {nomevelho} e tem {velho} anos')
print(f'A media de idade do grupo é {cont1 / 4} \nhá {cont} mulheres menores que 20 anos.')
