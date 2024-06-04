valores = []

condicao = 'S'
while condicao == 'S':
    valor = (int(input('Digite um valor: ')))
    if valor in valores:
        print('\033[34mValor duplicado! Não vou adicionar...\033[m')
    else:
        print('Valor adicionado com sucesso...')
        valores.append(valor)
        condicao = str(input('Quer continuar? [S/N] ')).upper()

valores.sort()
print('-=' * 30)
print(f'Os valores digitados foram: \033[32m{valores}\033[m')
print()
print('FIM DO PROGRAMA!')