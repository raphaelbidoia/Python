n1 = float(input('Fale Sua velocidade: '))
if n1 <= 80:
    print('Pode Seguir viagem!')
else:
    print(f'Você foi multado em R$: {(n1 - 80)*7}')
