import time
from time import sleep

n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
opcao= int(input('informe o numero maior que 0  '))
while opcao > 0:
    print('''[1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')

    opcao = int(input('>>>>> Qual é a sua opção? '))

    if opcao == 1:
        soma = n1 + n2
        print('O valor da soma é:', soma)
    elif opcao == 2:
        operacao = n1 * n2
        print('O valor da multiplicação é:', operacao)
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
        else:
            maior = 'Os dois valores são iguais'
        print('O maior valor é:', maior)
    elif opcao == 4:
        n1 = int(input('Informe o primeiro valor: '))
        n2 = int(input('Informe o segundo valor: '))
        print('Novos números foram informados.')
    else:
        print('Opção inválida. Tente novamente.')

    print('=-=' * 10)
    sleep(2)

print('Fim do programa! Volte sempre!')
