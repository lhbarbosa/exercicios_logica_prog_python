lista_palavra = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
               'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for palavra in lista_palavra:
<<<<<<< HEAD
    print(f'\nNa palavra \033[33m{palavra.upper()}\033[m temos ', end='')
    for vogais  in palavra:
        if vogais.lower() in 'aeiou':
            print(f'\033[32m{vogais}\033[m', end=' ')
print()
=======
   print(f'\nNa palavra \033[33m{palavra.upper()}\033[m temos ', end='')
   for vogais in palavra:
      if vogais.lower() in 'aeiou':
         print(f'\033[32m{vogais}\033[m', end=' ')
print()
>>>>>>> f40d399772f65d8f4b4440deaa08f0712ab0e8d5
