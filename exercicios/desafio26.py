
print('===== PRIMEIRA E ÚLTIMA OCORRÊNCIA DE UMA STRING =====')

name = input('Digite um frase: ').upper().strip()
print(f'A letra A aparece {name.count('A')} vezes na frase.')
print(f'A primeira letra A aparece na posição {name.find('A')+1}')
print(f'A última letra A aparece na posição {name.rfind('A')+1}')
