frase = str(input('''digite uma frase que possa ser lida
igual de frete para tras e de tras para frete: ''')).strip().upper()
p = frase.split()
j = frase.replace(' ', '')
i = ''
for letra in range(len(j)-1, -1, -1):
    i += j[letra]
print(f'O inverso de {j} é {i}')
if i == j:
    print('Temos um Políndromo')
else:
    print('A Frase não é um Políndromo')

