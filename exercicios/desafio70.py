print('{:-^40}'.format(' LOJAS PITUCHA '))
print()

total = maisMil = menorPreco = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: ')).strip().capitalize()
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco    
    if preco > 1000:
        maisMil += 1
    if cont == 1 or preco < menorPreco:
        menorPreco = preco
        barato = produto    
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Desja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print()
print('{:-^40}'.format(' TOTAL DAS COMPRAS '))
print(f'O total gasto foi R${total:.2f}')
print(f'Temos {maisMil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menorPreco:.2f}')

print()
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print()
