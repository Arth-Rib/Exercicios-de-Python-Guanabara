print('=-' * 30)
print(f'{"CADASTRO DE PESSOA":^30}')
print('=-' * 30)
somah = maiori = mm20 = 0
while True:
    i = int(input('Qual a idade da pessoa? '))
    while True:
        s = str(input('[M] para masculino\n[F] para feminino\nQual a sexo da pessoa? ')).strip().upper()
        if s in 'MF':
            break
        else:
            print('Selecione uma das opções!')
    if s == 'M':
        somah += 1
    if s == 'F' and i < 20:
        mm20 += 1
    if i > 18:
        maiori += 1
    print('=-' * 30)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    print('=-' * 30)
    if continuar in 'N':
        break
print(f'Tem {maiori} pessoa(s) com mais de 18 anos.\nForam cadastradas {somah} homem(ns).\nForam cadastradas {mm20} mulher(es) com menos de 20 anos.')