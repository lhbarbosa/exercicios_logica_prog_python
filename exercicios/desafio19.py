import random

name_1 = str(input('Primeiro aluno: '))
name_2 = str(input('Segundo aluno: '))
name_3 = str(input('Terceiro aluno: '))
name_4 = str(input('Quarto aluno: '))
lista = [name_1, name_2, name_3, name_4]
sorteado = random.choice(lista)
print(f'O aluno escolhido foi: {sorteado}')
