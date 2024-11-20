nome = str(input('digite teu nome completo: '))
n1 = nome.split()[0]
n2 = nome.rsplit()[-1]
print(f'Seu primeiro nome é {n1}, e seu ultimo nome é {n2}')
