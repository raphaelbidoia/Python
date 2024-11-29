cont = 0
cont2 = 0
from datetime import date
n1 = date.today().year
for c in range(1, 8):
    n = int(input(f'Em que ano a {c}º pessoa nasceu: '))
    n3 = n1 - n
    if n3 > 18:
        cont2 += 1
    if n3 < 18:
        cont += 1
print(f'tem {cont2} pessoas maiores de idade e {cont} menores de idade')




