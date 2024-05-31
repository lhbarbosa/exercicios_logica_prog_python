primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
count = 1
total = 0
mais = 10
while mais != 0: 
    total = total + mais
    while count <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        count += 1
    print('Pausa')
    mais = int(input('Quantos termos a mais você deseja? '))
print(f'Fim da PA total de termos mostrados {total}')
