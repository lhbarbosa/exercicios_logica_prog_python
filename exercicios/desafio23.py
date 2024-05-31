
print('===== Separando dígitos de um número =====\n')

number = int(input('Informe um número: '))
uni = number // 1 % 10
den = number // 10 % 10
cent = number // 100 % 10
mil = number // 1000 % 10

print(f'Analisando o número {number}')
print(f'Unidade: {uni}')
print(f'dezena: {den}')
print(f'Centena: {cent}')
print(f'Milhar: {mil}\n')
