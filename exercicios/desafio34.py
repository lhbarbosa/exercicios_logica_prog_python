
print("===== Aumentos múltiplos =====\n")

sal = float(input('Iforme o salário do funcioário: R$ '))

if sal > 1250:
    newSal = ((10 / 100) * sal) + sal
else:
    newSal = ((15 / 100) * sal) + sal
print(f'Novo salário é de R$ {newSal}')