nome=(input('digite seu nome completo: '))
n = (nome.upper())
print('seu nome maiusculo é {}'.format(n))
n0 = (nome.lower())
print('seu nome minusculo é {}'.format(n0))
n1 = nome.replace(" ", "")
print('seu nome tem no total {} letras'.format(len(n1)))
n2 = (nome.split()[0])
print('Seu primeiro nome é {} e ele tem {} letras'.format(n2, len(n2)))
