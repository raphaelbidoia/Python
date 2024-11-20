n1 = float(input('Digite seu salario: R$'))
if n1 > 1250:
    print(f'Você teve um aumneto de :R$ {(n1 * 10/100)+n1}')
else:
    print(f'Você teve um aumento de: R$ {(n1 * 15/100)+n1}')
