print('-=' * 20)
print('     Índice de Massa Corporal        ')
print('-=' * 20)
print('\n')

print('-=' * 20)
print('     TABELA DE IMC       ')
print('-=' * 20)
print("""
- Abaixo de 18.5: Abaixo do peso
- Entre de 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
\n""")

peso = float( input('Informe seu peso? (kg) ') )
altura = float( input('Informe sua altura (m): ') )

imc = peso / (altura ** 2)


if imc < 18.5:
    print(f'Você está ABAIXO DO PESO!\nSeu IMC: {imc:.2f}\n')
elif imc <= 18.5 or imc < 25:
    print(f'Você está no peso IDEAL!\nSeu IMC: {imc:.2f}\n')
elif imc <= 25 or imc < 30:
        print(f'Você está com SOBRE PESO!\nSeu IMC: {imc:.2f}\n')
elif imc <= 30 or imc < 40:
        print(f'Você está com OBESIDADE!\nSeu IMC: {imc:.2f}\n')
else:
    print(f'Você está com OBESIDADE MÓRBIDA!\nSeu IMC: {imc:.2f}\n')
