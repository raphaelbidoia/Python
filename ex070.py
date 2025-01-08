'''c = s = t = 0
menor = 0
n = input('iniciar o programa [S/N]: ')
while n in 'Ss':
    nome = input('qual o produto: ')
    preco = float(input('valor do produto R$: '))
    c += preco
    if preco > 1000:
        s += 1
    if 0 == preco:
        menor = preco
    else:
        menor = preco
    n = input('continuar?[S/N] ')
print(f'o valor do produto mais barado é R${menor} tiveram:{s} produtos acima de 1000,00 reais\no total da compra foi R$:{c}')'''
total = tp = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Qual o valor do produto: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        tp += 1
    if cont == 1 or preco > menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('quer continuar: [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'acabou, o total da compra foi de R${total:.2f} produtos maior que mil reais {tp}, o produto mais barato é {barato} e custa R${menor}')