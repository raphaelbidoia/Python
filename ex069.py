'''h = i = s = 0
print('Cadastro de idade e sexo: ')
n = input('ligar o programa [S/N] ')
while n in 'Ss':
    print('cadastro')
    n = input('quer cadastrar alguem [S/N] ')
    idade = int(input('Qual sua idade: '))
    sexo = input('sexo [M/F]:')
    if idade < 18:
        h += 1
    if sexo in 'Mm':
        s += 1
    if sexo in 'Ff' and idade < 20:
        i += 1
print(f'Há {h} pessoas com menos de 18 há {s} homens e há {i} mulheres com menos de 20 anos ')'''
t18 = tm = tf = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o Sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        t18 +=1
    if sexo == 'M':
        tm += 1
    if sexo == 'F' and idade < 20:
        tf += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Acabou. Total de pessoas com mais de 18 anos: {t18}, Homens cadasdrados {tm} e temos {tf} mulheres com menos de 20 anos.')
