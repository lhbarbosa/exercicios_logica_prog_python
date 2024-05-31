from datetime import date

atual = date.today().year
maior = 0
menor = 0
for pess in range(1, 8):
    ano_nasc = int(input(f'Digite o ano de nascimento da {pess}ª pessoa: '))
    idade = atual - ano_nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'Ao todo temos {maior} pessoas maiores de idade')
print(f'Ao todo temos {menor} pessoas menores de idade\n')
