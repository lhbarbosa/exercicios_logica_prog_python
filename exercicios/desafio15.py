
print('===== Aluguel de Carros =====\n')
day = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
totalDay = day * 60
km_driven = km * 0.15
total_paid = totalDay + km_driven
print(f'O total a pagar é de R$ {total_paid}\n')
