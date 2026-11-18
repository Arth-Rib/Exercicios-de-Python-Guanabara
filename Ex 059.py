op = 0
while op != 5:
    n1 = float(input('Primeiro valor: '))
    n2 = float(input('Segundo valor: '))
    print('\033[4mDigite uma das opções abaixo.\033[m\n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos\n[5]Sair')
    op = int(input('Selecione:'))
    if op == 1:
        soma = n1 + n2
        print('A soma de {} e {} é: {}'.format(n1, n2, soma))
    if op == 2:
        mult = n1 * n2
        print('A multiplicação de {} e {} é: {}'.format(n1, n2, mult))
    if op == 3:
        if n1 > n2:
            print('O maior numero entre {} e {} é: {}'.format(n1, n2, n1))
        if n1 < n2:
            print('O maior numero entre {} e {} é: {}'.format(n1, n2, n2))
    if op == 4:
        print('Excluindo numeros antigos e solicitando novos!')
    if op != 1 and op != 2 and op != 3 and op != 4 and op != 5:
        print('Selecione uma das opções validas!')
print('Fim do programa')