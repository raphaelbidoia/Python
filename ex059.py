'''print('Digite dois valores: ')
print('==='*20)
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
print('Digite a função que gostaria:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos numeros
[5] Sair')
print('==='*20)
n = int(input('digite uma das Opções: '))
if n == 1:
    n3 = n1 + n2
    print('===' * 20)
    print(f'A soma dos numeros é: {n3}')
if n == 2:
    n4 = n1 * n2
    print('===' * 20)
    print(f'a multiplicação entre os numeros é {n4}')
if n == 3:
    n1 > n2
    print('===' * 20)
    print(f'O maior é {n1}')
    if n2 > n1:
        print('===' * 20)
        print(f'O maior é {n2}')
while n != 5:
    print('Digite dois valores: ')
    print('===' * 20)
    n1 = int(input('Primeiro Valor: '))
    n2 = int(input('Segundo Valor: '))
    print('===' * 20)
    print('Digite a função que gostaria:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair')
    print('===' * 20)
    n = int(input('digite uma das Opções: '))
    if n == 1:
        n3 = n1 + n2
        print('===' * 20)
        print(f'A soma dos numeros é: {n3}')
    if n == 2:
        n4 = n1 * n2
        print('===' * 20)
        print(f'a multiplicação entre os numeros é {n4}')
    if n == 3:
        n1 > n2
        print('===' * 20)
        print(f'O maior é {n1}')
        if n2 > n1:
            print('===' * 20)
            print(f'O maior é {n2}')
print('==='*20)
print('Muito obrigado por usar nosso programa')'''
#professor
n1 = int(input('digite o primeiro valor: '))
n2 = int(input('digite o segundo valor: '))
opção = 0
while opção != 5:
    print(''' opções
        [1] Soma
        [2] Multiplicação
        [3] Maior
        [4] Digitar novamente
        [5] Sair''')
    opção = int(input('digite uma das opções: '))
    if opção == 1:
        soma = n1 + n2
        print(f'a soma de {n1} + {n2} é {soma}')
    elif opção == 2:
        multiplicar = n1 * n2
        print(f'A multiplicação dos numeros {n1} X {n2} é {multiplicar}')
    elif opção == 3:
        if n1>n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}')
    elif opção == 4:
        print('Digite novamente:')
        n1 = int(input('digite o primeiro valor: '))
        n2 = int(input('digite o segundo valor: '))
    elif opção == 5:
        print('Saindo...')
    else:
        print('opção invalida')