from datetime import date
ano = int(input('Por Favor digite seu ano de nascimento: '))
n1 = date.today().year
print(f'Você tem {n1 - ano} anos:')
if n1 - ano == 18:
    print('Você tem 18 anos esse ano você se alista')
elif n1 - ano > 18:
    saldo = n1 - ano - 18
    print(f'Você ja completou 18 anos e esta atrasado em \033[31m{saldo}\033[m para se alistar')
    print(f'seu ano de alistamento foi em {n1 - saldo}')
elif n1 - ano < 18:
    saldo = ((n1 - ano - 18) * -1)
    print(f'Você ira fazer 18 anos, faltam: \033[34m{saldo}\033[m para se alistar')
    print(f'seu ano de alistamento sera em {saldo + n1}')
