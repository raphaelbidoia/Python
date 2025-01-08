
print('digite um numero negativo para parar')
n = int(input('Digite um numero: '))
while n >= 0:
    for c in range(1, 11):
        print(f' {n} X {c} = {n*c}')
    n = int(input('Digite um numero: '))
print('tabuada encerrada')
