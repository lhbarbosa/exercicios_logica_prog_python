num = int(input('Digite um número para calcula o fatorial: '))

count = num
fact = 1
print(f'\nResultado {num}! = ', end='')
while count > 0:
    print(count, end='')
    print(' x ' if count > 1 else ' = ', end='' )
    fact *= count
    count -= 1
print(f'{fact}\n')

