import random
number = random.randint(0, 10)

print('========== Jogo de Adivinhação v2.0 ==========')
print('VAMOS JOGAR...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?.')
cont = 0
acerto = False
while not acerto:
    num = int(input('Qual seu palpite? '))
    cont += 1
    if num == number:
        acerto = True
    else:
        if num < number:
            print('Mais... Tente mais uma vez.')
        elif num > number:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {cont} tentativas. Parabéns!')
