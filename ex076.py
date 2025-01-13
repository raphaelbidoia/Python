listagem = ('lapis', 1.99,
            'borracha', 2.39,
            'caneta', 2.99,
            'estojo', 7.99,
            'mochila', 99.99,
            'caderno', 14.99,
            'folhas', 5.99,
            'livro', 79.89)
print('=' * 50)
print(f'{"LISTA DE COMPRAS":^40}')
print('=' * 50)
for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}', end=' ')
    else:
        print(f'R$ {listagem[item]:>7}')
print('=' * 50)
