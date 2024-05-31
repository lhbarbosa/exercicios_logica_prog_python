
print('-=' * 20)
print('     Conversor de Bases Numéricas    ')
print('-=' * 20)
print('\n')

num = int(input('Informe o número inteiro: '))
print("""Escolha qual a base de conversão que deseja
[ 1 ] Binária
[ 2 ] Octal
[ 3 ] Hexadecimal""")
opcao = int(input('Qual sua opção: '))

if opcao == 1:
    print(f'A conversão de {num} Decimal para Binário {bin(num)[2:]}')
elif opcao == 2:
    print(f'A conversão de {num} Decimal para Octal {oct(num)[2:]}')
elif opcao == 3:
    print(f'A conversão de {num} Decimal para Hexadecimal {hex(num)[2:]}')
else:
    print('Opção inválida. Tente novamente.')
