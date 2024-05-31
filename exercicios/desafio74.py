from random import randint

num_sorteados = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os números sorteados foram: {num_sorteados}')
print(f'O maior valor encontrado foi: {max(num_sorteados)}')
print(f'O menor valor encontrado foi: {min(num_sorteados)}')
