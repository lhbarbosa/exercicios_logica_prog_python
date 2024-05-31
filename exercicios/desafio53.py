frase = str(input('Digite uma frase: ')).strip().upper()
palvras = frase.split()
junto = ''.join(palvras)
inverso = junto[::-1]
print(f'O inverso de {frase} é {inverso}')
if inverso == junto:
    print('Então é um PALINDROMO!')
else:
    print('Então NÃO É UM PALINDROMO!')