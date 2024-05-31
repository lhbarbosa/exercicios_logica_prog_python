produtos = (('Lápis', 1.75), 
            ('Borracha', 2), 
            ('Caderno', 15.90), 
            ('Estojo', 25), 
            ('Transferidor', 4.20), 
            ('Compasso', 9.99), 
            ('Mochila', 120.32), 
            ('Canetas', 22.30), 
            ('Livro', 34.90))

print('-'*42)
print('{:^40}'.format('Listagem de Preços'))
print('-'*42)

for produto, preco in produtos:
    print(f'{produto:.<30} R$ {preco:>6.2f}')

print('-'*42)


''' Resolução Prof. 
produtos = ('Lápis', 1.75, 
            'Borracha', 2, 
            'Caderno', 15.90, 
            'Estojo', 25, 
            'Transferidor', 4.20, 
            'Compasso', 9.99, 
            'Mochila', 120.32, 
            'Canetas', 22.30, 
            'Livro', 34.90)

print('-'*40)
print('{:^40}'.format('Listagem de Preços'))
print('-'*40)

for produto in range(len(produtos)):
    if produto % 2 == 0:
        print(f'{produtos[produto]:.<30}', end="")
    else:
        print(f'R$ {produtos[produto]:>7.2f}')
print('-'*40)
'''