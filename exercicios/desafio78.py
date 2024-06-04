valores = []

for posicao in range(0, 5):
    valores.append(int(input(f'Digite um valor para posição {posicao}: ')))

print('=-' * 30)
print(f'Você digitou os valores {valores}')

print(f'O \033[32mMAIOR valor digitado foi {max(valores)}\033[m e está nas posições ', end='')
for pos, chave in enumerate(valores):
    if chave == max(valores):
        print(f'\033[33m{pos}\033[m...',end='')
print()

print(f'O \033[32mMENOR valor digitado foi {min(valores)}\033[m e está nas posições ', end=' ')
for pos, chave in enumerate(valores):
    if chave == min(valores):
        print(f'\033[33m{pos}\033[m...', end='')
print('\n')
