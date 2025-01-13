numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
cliente = int(input('Digite um numero de 0 a 20: '))
for valor in range(cliente-1, cliente):
    print(f'Você digitou o numero {numero[valor+1]}')