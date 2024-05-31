import math

catetoOposto = float(input('Digite o valor do cateto oposto: '))
catetoAdjacente = float(input('Digite o valor do cateto adjacente: '))
hip = math.sqrt(catetoOposto**2 + catetoAdjacente**2)
print(f'O resultado da hipotenusa é: {hip:.2f}')