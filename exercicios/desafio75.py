tupla_valores = (int(input('Digite um número: ')),
               int(input('Digite outro número: ')),
               int(input('Digite mais um número: ')),
               int(input('Digite um último número: ')))

print(f'Você digitou os seguites valores: {tupla_valores}')
print(f'O valor 9 apareceu {tupla_valores.count(9)} vezes')

if 3 in tupla_valores:
   print(f'O valor 3 apareceu na posição {tupla_valores.index(3) + 1}ª')
else:
   print(f'O valor 3 não foi digitado!')

print(f'Os valores pares dos números digitados foram: ', end='')
for n in tupla_valores:
   if n % 2 == 0:
      print(n, end=' ')
print()
