
print("===== RADAR ELETRÔNICO =====\n")

vel = int(input('Digite a velocidade do veiculo: '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Ultrapassou o limite de velocidade. Você foi multado!')
    print(f'Valor da multa R$ {multa:.2f}')
else:
    print('Boa viagem, dirija com cuidado!')
