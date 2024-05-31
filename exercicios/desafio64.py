cont = soma = number = 0
number = int(input('Digite um número [999 para parar]: '))
while number != 999:
    cont += 1
    soma += number
    number = int(input('Digite um número [999 para parar]: '))

print('~'*40)
print(f'Total de números digitados: {cont}')
print(f'Total da soma entre os números: {soma}')
print('FIM DO PROGRAMA!\n')
