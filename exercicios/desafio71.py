print('=' * 30)
print('{:^35}'.format('\033[32mBANCO SOR\033[m'))
print('=' * 30)

valor = int(input('Que valor você quer sacar? R$'))
print()
total = valor
ced = 50
totalNotas = 0

while True:
    if total >= ced:
        total -= ced
        totalNotas +=1
    else:
        if totalNotas > 0:
            print(f'Total de {totalNotas} cédulas de R$ {ced}')
        elif ced == 500:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalNotas = 0
        if total == 0:
            break

print('\nObrigado! Volte sempre.\n')

