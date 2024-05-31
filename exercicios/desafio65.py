stop = 'S'
cont = soma = maior = menor = media = 0

while stop == 'S':
    number = int(input('Digite um número: '))
    stop = str(input('Quer continuar? [S/N]: ')).upper()
    cont += 1
    soma += number
    if cont == 1:
        maior = menor = number
    else:
        if number > maior:
            maior = number
        if number < maior:
            menor = number

media = soma / cont
print(f'- O total de números digitados é: {cont}')
print(f'- A média entre os números é: {media:.2f}')
print(f'- O maior valor foi {maior} e o menor foi {menor}')
print('\nFIM DO PROGRAMA!')
