print('Para saber o seu peso ideal digite: ')
a = float(input('Digite sua altura: '))
p = float(input('Digite seu peso: '))
n = p / (a**2)
print(n)
if n <= 18.5:
    print('Abaixo do peso')
elif 18.5 <= n < 25:
    print('Peso ideal')
elif 25 <= n < 30:
    print('Sobrepeso')
elif 30 <= n < 40:
    print('Obesidade')
elif n >= 40:
    print('Obesidade Morbida')

