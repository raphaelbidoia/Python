c = s = 0
n = int(input('ditite 999 para parar com a seguencia\nDigite um numero:'))
while n != 999:
    c += 1
    s += n
    n = int(input('digite um numero:'))
print(f'Você digitou {c} numeros e a soma é {s}')
