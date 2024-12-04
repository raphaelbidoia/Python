n = s = c = 0
print('Digite o numero que quer somar e')
print('digite 999 para parar.')
n = int(input('Digite o numero desejado: '))
while n != 999:
        s += n
        c += 1
        print('==='*10)
        n = int(input('Digite o numero desejado: '))
print(f'A soma de todos os numeros foi de \033[32m{s}\033[m\nforam digitados \033[32m{c}\033[m numeros.')
print('+++' *20)
print('\033[32mObigado por usar!')
