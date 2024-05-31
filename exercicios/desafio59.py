from time import sleep

print('-=' * 20)
print('     Criando um Menu de opções       ')
print('-=' * 20)

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
    opcao = int(input('>>> Qual a sua opção? '))
    if opcao == 1:
        resultado = num1 + num2
        print(f'O resultado de {num1} + {num2} = {resultado} ')
        print('-==' * 15)
    elif opcao == 2:
        resultado = num1 * num2
        print(f'O resultado de {num1} x {num2} = {resultado}')
        print('-==' * 15)
    elif opcao == 3:
        if num1 > num2:
            print(f'Entre {num1} e {num2} o maior é {num1}')
            print('-==' * 15)
        elif num2 > num1:
            print(f'Entre {num1} e {num2} o maior é {num2}')
            print('-==' * 15)
        else:
            print(f'Entre {num1} e {num2} não temos maior ambos são iguais')
            print('-==' * 15)
    elif opcao == 4:
        print('Informe os números novamente: ')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
        print('-==' * 15)
    elif opcao == 5:
        print('Finalizando...')
        print('-==' * 15)
        sleep(2)
    else:
        print('Opção inválida. Tente novamente.')
        print('-==' * 15)
print('Fim do programa! Volte sempre!')
