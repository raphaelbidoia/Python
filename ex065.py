n = 1
s = c = 0
print('digite os valores desejado para saber sua media\nou digite\033[31m 0\033[m para sair')
while n != 0:
    n = int(input('digite o numero:'))
    if n != 0:
        s += n
        c += 1
        if c == 1:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
print(f'a media entre os valores é de {s/c}')
print(f'e o {maior} foi o maior e o {menor} foi o menor. ')
