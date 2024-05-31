from time import sleep

while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    
    if num < 0:
        break
    
    print('-'*20)
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
    print('-'*20)

print('ENCERRADNDO...')
sleep(1)
print(f'Programa Encerrado! Volte sempre!\n')
