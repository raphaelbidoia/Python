n1 = float(input('Digite a distancia de sua viagem em km: '))
print(f'a distamcia é {n1} KM')
if n1 <= 200:
    print(f'O valor de seu pedágio é R$: {n1 * 0.50}')
else:
    print(f'O valor de seu pedágio é R$: {n1 * 0.45}')
