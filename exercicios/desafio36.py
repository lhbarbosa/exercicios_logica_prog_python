
print('-=' * 20)
print('         Aprovando Empréstimo            ')
print('-=' * 20)
print('\n')

valorCasa = float( input('Qual o valor da casa: R$') )
sal = float( input('Qual o salário do comprador: R$') )
ano = int( input('Quantos anos de financiamento? ') ) 

prest =   valorCasa / (ano * 12)
minimo = ( 30 / 100 ) * sal

print(f'Para pagar uma casa de R${valorCasa:.2f} em {ano} anos a prestação será de R${prest:.2f}')

if prest <= minimo:
    print('Financiamento APROVADO!')
else:
    print('Financiamento NEGADO!')
