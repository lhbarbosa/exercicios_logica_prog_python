
print("===== Ano Bissexto =====\n")

ano = int(input('Digite um ano qualquer: '))
if ano % 4 == 0:
    print(f'O ano de {ano} é Bissexto')
else:
    print(f'O ano de {ano} não é Bissexto')