
import random
number = random.randint(0, 5)

print('========== Jogo de Adivinhação ==========')

print('VAMOS JOGAR...')
num = int(input('Escolhar um número entre 0 e 5: '))
if num == number:
    print(f'Você VENCEU! número que pensei: {number}')
else:
    print(f'Você PERDEU!\nTente novamente. número que pensei: {number}')



