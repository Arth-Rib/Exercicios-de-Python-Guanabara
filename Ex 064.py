n = 0
c = 0
soma = 0
while n != 999:
    print('Digite 999 para encerrar.')
    n = int(input('Digite o valor que deseja somar: '))
    if n != 999:
        c += 1
        soma += n
    print('-'*40)
print('Você digitou {} números e a soma deles é {}.'.format(c, soma))