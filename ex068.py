from random import randint
'''perdeu = False
c = s = 0
while not perdeu:
    print('Vamos Jogar Par ou Impar!')
    n2 = int(input('[1] Par
[2] Impar
digite qual quer escolher: '))
    n = int(input('Jogue um numero: '))
    computador = randint(0, 10)
    n1 = n + computador
    print(f'a soma dos nossos numeros foi {n1}')
    c += 1
    if n2 == 1 and n1 % 2 == 0:
        print('então ele é Par')
    if n2 == 2 and n1 % 2 == 1:
        print('então ele é Impar')
    else:
        if n2 == 1 and n1 % 2 == 1:
            perdeu = True
            print('você perdeu')
        s += 1
print(f'Você venceu o computardor {c - 1} vezes')'''
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você Jogou {jogador} e o computador {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Ganhou!!')
            v += 1
        else:
            print('Você Perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Ganhou!')
            v += 1
        else:
            print('Você Perdeu!')
            break
    print('JOGUE NOVAMENTE!')
print(f'Você Ganhou do computador {v} Vezes! Parábens!')
