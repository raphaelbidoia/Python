n1 = int(input('digite um numero: '))
n2 = int(input('digite um numero: '))
n3 = int(input('digite um numero: '))
n4 = int(input('digite um numero: '))
lista = (n1, n2, n3, n4)
print(f'Voce digitou {lista}')
print(f'o numeor 9 parareceu {lista.count(9)}')
print(f'o numero 3 foi digitado na {lista.index(3)+1}ª posição')
for n in lista:
    if n % 2 == 0:
        print(f'o numero par digitado foi {n}')