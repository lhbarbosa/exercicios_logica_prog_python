
print('-=' * 20)
print('         MÉDIA ALUNO         ')
print('-=' * 20)
print('\n')

nota_1 = float( input('Informe a primiera nota: ') )
nota_2 = float( input('Informe a segunda nota: ') )
media = (nota_1 + nota_2) / 2

if media < 5.0:
    print(f'Aluno REPROVADO! \nNota Final: {media:.1f}\n')
elif media == 5.0 or media <= 6.9:
    print(f'Aluno de RECUPERAÇÃO! \nNota Final: {media:.1f}\n')
else:
    print(f'Aluno de APROVADO! \nNota Final: {media:.1f}\n')

