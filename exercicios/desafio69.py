mais18 = totM20 = totHomens = 0

while True:
    print('-'*40)
    print('           CADASTRE UMA PESSOA')
    print('-'*40)
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [M/F]? ')).strip().upper()[0]
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        totHomens +=1
    if sexo == 'F':
        if idade < 20:
            totM20 += 1
    
    print('-'*40)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja cadastrar mais pessoa? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break

print('-'*20)
print(f'Temos {mais18} pessoas maior de 18 anos. ')
print(f'Temos {totHomens} homens cadastrados. ')
print(f'Temos {totM20} mulheres com menos de 20 anos.\n')
