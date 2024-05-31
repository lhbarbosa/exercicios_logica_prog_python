print('=' * 15,' TABUADA v.2.0 ', '=' * 15)

inicio = int(input('Digite um número para ver sua tabuada: '))

print('='*4, 'RESULTADO','='*4)
for x in range(1, 10 + 1):
    result = inicio * x
    print(f'    {inicio} x {x} = {result}')
print('='*20)

