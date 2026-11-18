'''r = 'S'
while r == 'S':
    n = int(input('Digite um numero: '))
    r = str(input('Quer continuar? [S/N] : ')).upper()
print('Fim')'''
n1 = 1
par = impar = 0
while n1 != 0:
    n1 = int(input('Digite um numero: '))
    if n1 != 0:
        if n1 % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares'.format(par, impar))
