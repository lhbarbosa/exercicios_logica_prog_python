num = int(input('Digite um número: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {num} foi divisível {cont} vezes')
if cont == 2:
    print('e por isso É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
