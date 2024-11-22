print( '=+=+' * 20)
print('Boa tarde, por favor digite o valor do Imóvel, renda '
      '\ne quantos anos gostaria de financiar:')
print('=+=+' * 20)
casa = int(input('valor do Imóvel: R$'))
renda = float(input('Valor do salario: R$'))
anos = int(input('Quantos anos: '))
prest = (anos * 12)
parc = casa // prest
if parc > renda * 30/100:
    print('\033[0;33mRECUSADO\033[m Por Favor, Reduza o valor do imovel')
    print(f'O valor da parcela ficou R${parc} que excede seu limite')
elif parc <= renda * 30/100:
    print('\033[32mAPROVADO\033[m Por Favor de continuidade com nossos atendentes')
    print(f'a Quandidade de parcelas ficou em {prest}X no valor de R${parc}')
