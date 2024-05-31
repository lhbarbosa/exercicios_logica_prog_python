
print("===== Custo de Viagem =====\n")

dist = int(input('Informe a distância da viagem: '))
if dist <= 200:
    custo = dist * 0.5
    print(f'Custo total da viagem é de R$ {custo:.2f}')
else:
    custo = dist * 0.45
    print(f'Custo total da viagem é de R$ {custo:.2f}')





