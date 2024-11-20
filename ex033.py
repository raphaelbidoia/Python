print('Digite 3 valores')
n1 = int(input('Primeiro Numero: '))
n2 = int(input('Segundo Numero: '))
n3 = int(input('Terceiro Numero: '))
if n1 > n2 and n1 > n3:
    print(f'o maior foi: {n1}')
if n2 > n1 and n2 > n3:
    print(f'o maior foi: {n2}')
if n3 > n1 and n3 > n2:
    print(f'o maior foi: {n3}')
#menor
if n1 < n2 and n1 < n3:
    print(f'o menor foi: {n1}')
if n2 < n1 and n2 < n3:
    print(f'o menor foi: {n2}')
if n3 < n2 and n3 < n1:
    print(f'o menor foi: {n3}')
