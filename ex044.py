print('Digite o valor e o metodo de pagamento: ')
n = float(input('valor da compra: R$'))
print('=='*20)
n1 = float(input('\033[40mFormas liberadas:::\033[m\n'
                 '\033[32mA Vista\033[m, digite: 1\n'
                 '\033[34mCartão a vista\033[m, digite: 2\n'
                 '\033[36mParcelado em ate 2X\033[m, digite: 3\n'
                 '\033[31mParcelado em 3X ou mais\033[m digite: 4\n'
                 'digite a forma de pagamento: '))
print('=='*20)
if n1 == 1:
    print('método de pagamento a vista Dinheiro ou Cheque:')
    print(f'O valor de Sua compra é: R${n - (n * 10//100)} com 10% de desconto!')
elif n1 == 2:
    print('método de pagamento a vista Cartão: ')
    print(f'O valor de Sua compra é: R${n - (n * 5//100)} com 5% de desconto!')
elif n1 == 3:
    print('método de pagamento Parcelado em ate 2X:')
    y = n // 2
    print(f'E as Parcelas ficaram em 2X de R${y}')
    print(f'O valor da sua Compra fica em {n}')
elif n1 == 4:
    n0 = int(input('quantas parcelas?'))
    print('método de pagamento Parcelado em 3X ou mais:')
    p = n + (n * 20//100)
    t = p // n0
    print(f'E as Parcelas ficaram em {n0}X de R${t}')
    print(f'O valor da Sua Compra fica; R${p}')
else:
    print('opção invalida')
