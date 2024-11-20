print('Digite 3 valores para saber se eles formarão um triangulo:')
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo Valor: '))
n3 = float(input('Terceiro valor: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n1:
    print('é um triangulo')
else:
    print('não é um triangulo')
