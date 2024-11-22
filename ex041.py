from datetime import date
ano = int(input('Por Favor digite seu ano de nascimento: '))
n1 = date.today().year
print(f'Você tem {n1 - ano} anos:')
if n1 - ano <= 9:
    print('Você 9 anos ou menos Você é um Atleta Mirim')
elif n1 - ano <= 14:
    print(f'Você 14 anos ou menos Você é um Atleta Infantilr')
elif n1 - ano <= 19:
    print(f'Você 19 anos ou menos Você é um Atleta Junior')
elif n1 - ano <= 24:
    print(f'Você 20 anos ou menos Você é um Atleta Sênior')
elif n1 - ano >= 25:
    print(f'Você 21 anos ou mais Você é um Atleta Master')
