r = str(input('Sexo [M/F]: ')).strip()
while r not in 'MmFf':
    print(' Erro no registro, digite novamente')
    r = str(input('Sexo [M/F]: ')).strip()
print('sexo registrado, obrigado')
