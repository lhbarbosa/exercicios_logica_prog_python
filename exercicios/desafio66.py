cont = soma = 0 

num = int(input('Digite um número (para parar 999): '))
while True:
    cont += 1
    soma += num
    num = int(input('Digite um número (para parar 999): '))
    if num == 999:
        break

print('-='*20)
print(f'''O total de números digitos foi: {cont}
A soma dos números digitos foi: {soma}''')
print('-='*20)
print('FIM DO PROGRAMA')