print('=' * 15,' GAME: PEDRA / PAPEL / TESOURA ', '=' * 15)

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(
"""
Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura""")
jogador = int( input('Qual a sua jogada? ') )
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print('-=' * 15)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 15)

# Computador escolheu Pedra
if computador == 0:
    if jogador == 0:
        print('\033[0;33mEMPATE\033[m')
    elif jogador == 1:
        print('\033[0;42mJOGADOR VENCEU\033[m')
    elif jogador == 2:
        print('\033[0;35mCOMPUTADOR VENCEU\033[m')
    else:
        print('\033[0;31mJOGADA INVÁLIDA!\033[m')
    
# Computador escolheu Papel
elif computador == 1:
    if jogador == 0:
        print('\033[0;35mCOMPUTADOR VENCEU\033[m')
    elif jogador == 1:
        print('\033[0;33mEMPATE\033[m')
    elif jogador == 2:
        print('\033[0;42mJOGADOR VENCEU\033[m')
    else:
        print('\033[0;31mJOGADA INVÁLIDA!\033[m')

# Computador escolheu Tesoura
elif computador == 2:
    if jogador == 0:
        print('\033[0;42mJOGADOR VENCEU\033[m')
    elif jogador == 1:
        print('\033[0;35mCOMPUTADOR VENCEU\033[m')
    elif jogador == 2:
        print('\033[0;33mEMPATE\033[m')
    else:
        print('\033[0;31mJOGADA INVÁLIDA!\033[m')
