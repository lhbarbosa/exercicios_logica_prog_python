somaIdade = 0
nomeVelho = ''
idadeVelho = 0
totalMulher = 0

for p in range(1,5):
    print(f'_____ {p}ª PESSOA _______')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip()
    
    somaIdade += idade
    if p == 1 and sexo in 'Mn':
        idadeVelho = idade
        nomeVelho = nome
    if sexo in 'Mn' and idade > idadeVelho:
        idadeVelho = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totalMulher += 1
    
mediaIdade = somaIdade / 4
print(f'A média de idade do grupo é: {mediaIdade} anos.')
print(f'O nome do Homem mais velho é: {nomeVelho} e tem {idadeVelho} anos.')
print(f'O total de mulheres com menos de 20 anos é: {totalMulher}.')
