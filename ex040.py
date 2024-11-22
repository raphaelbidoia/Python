print('Aqui você sabe se reprovou ou se passou de ano:')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua Segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))

media = (n1 + n2 + n3) // 3.0
if media <= 5.0:
    print('\033[41mREPROVADO\033[m')
elif media <= 6.9:
    print('\033[43mRECUPERAÇÂO\033[m')
elif media >= 7.0:
    print('\033[42mAPROVADO\033[m')
print(f'Sua Média foi {media}')
