from datetime import date
n1 = int(input('Digite um Ano para saber se ele é Bissexto: \nOu coloque 0 para analizar o ano atual: '))
if n1 == 0:
    n1 = date.today().year
    print(f'O ano de {n1}')
if n1 % 4 == 0 and n1 % 100 !=0 or n1 % 400 ==0:
    print(f'O ano de {n1} é bissexto')
else:
    print(f'O ano de {n1} não é um ano bissexto')
