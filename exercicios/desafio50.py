print('=' * 15,' SOMA DOS PARES ', '=' * 15)

soma = 0
cont = 0
for c in range(1, 7):
    num1 = int(input(f'Digite o {c}º número: '))
    if num1 % 2 == 0:
        soma += num1
        cont += 1

print(f'Você informou {cont} valores PARES e a soma é: {soma}\n')
