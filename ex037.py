#escreva um programa que leia um valor e transforme em
#-binario
#-octal
#-hexadecimal

n = int(input('Digite um numero: '))
print('1 - binario')
print('2 - octal')
print('3 - hexadecimal')
n2 = int(input('Digite uma Opção: '))
if n2 == 1:
    nb = bin(n)[2:]
    print(f'Seu Numero em Binario é: {nb}')
elif n2 == 2:
    nb = oct(n)[2:]
    print(f'Seu numero em Octal é: {nb}')
elif n2 == 3:
    nb = hex(n)[2:]
    print(f'Seu numero em Hexadecimal é: {nb}')
else:
    print('opção invalida')
