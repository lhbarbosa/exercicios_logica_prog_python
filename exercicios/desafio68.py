from random import randint

print('=-'*20)
print('\033[33mVAMOS JOGAR PAR OU ÍMPAR\033[m')
print('=-'*20)

qtde = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(1, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I]? ')).upper().strip()[0]
    print('-'*20)
    print(f'Você jogou {jogador} e o computador {computador}. Total é {total} ', end='')
    print('\033[4;34mDEU PAR\033[m' if total % 2 == 0 else '\033[4;35mDEU ÍMPAR\033[m')
    print('-'*20)
    if tipo == 'P':
        if total % 2 == 0:
            print('\033[32mVocê VENCEU!\033[m')
            qtde += 1
            print('Vamos jogar novamente...')
        else:
            print('\033[31mVocê PERDEU!\033[m')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('\033[32mVocê VENCEU!\033[m')
            qtde += 1
            print('Vamos jogar novamente...')
        else:
            print('\033[31mVocê PERDEU!\033[m')
            break
    print('-'*20)

print('-='*20)
print(f'\033[35mGAME OVER! Você venceu {qtde} vezes.\033[m\n')