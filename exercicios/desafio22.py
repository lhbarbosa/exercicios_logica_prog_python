
print('===== Analisador de Textos =====')
name = input('Digite seu nome completo: ')
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {name.upper()}')
print(f'Seu nome em minúsculas é {name.lower()}')

neverSpaceName = name.replace(' ', '')
print(f'Seu nome tem ao todo {len(neverSpaceName)} letras')

firstName = name.split()
print(f'Seu primeiro nome é {firstName[0]} e ele tem {len(firstName[0])} letras')