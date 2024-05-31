print('=' * 15,' LOJAS BARBOSA ', '=' * 15)
preco = float( input('Preço das compras: R$') )
print("""Qual a forma de pagameto: 
[ 1 ] Dinheiro/Cheque 
[ 2 ] Á vista Cartão 
[ 3 ] 2x no Cartão 
[ 4 ] 3x ou mais no Cartão? """)
opcao = int(input('Qual é a opção: '))
if opcao == 1:
    total = preco - ((10 / 100) * preco)
elif opcao == 2:
    total = preco - ((5 / 100) * preco)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')
elif opcao == 4:
    total = preco + (preco * (20 / 100))
    totparc = int(input('Quantas parcela? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} COM JUROS')
else:
    total = 0
    print('\033[0;31mOPÇÃO INVÁLIDA\033[m de pagamento. Tente novamente!')
print(f'Sua compra de \033[0;36;42mR${preco:.2f}\033[m vai custar \033[0;32mR${total:.2f}\033[m no final.\n')






















