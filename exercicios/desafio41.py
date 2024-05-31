
print('-=' * 20)
print('Classificação Atleta')
print('-=' * 20)
print('\n')

from datetime import date
atual = date.today().year
nasc = int( input('Ano de Nascimento: ') )
idade = atual - nasc
print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Categoria do atleta é: MIRIM')
elif idade <= 14:
    print('Categoria do atleta é: INFANTIL')
elif idade <= 19:
    print('Categoria do atleta é: JUNIOR')
elif idade <= 20:
    print('Categoria do atleta é: SÊNIOR')
else:
    print('Categoria do atleta é: MASTER')
