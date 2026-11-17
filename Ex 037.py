n = int(input('Digite um numero inteiro: '))
a = int(input('Digite 1 para binario, 2 para octal e 3 para hexadecimal: '))
if a == 1:
    b = bin(n)[2:].upper()
    print('O numero {} em binário é {}.'.format(n,b))
elif a == 2:
    o = oct(n)[2:].upper()
    print('O número {} em octal é {}.'.format(n,o))
elif a == 3:
    h = hex(n)[2:].upper()
    print('O número {} em hexadecimal é {}.'.format(n,h))
else:
    print('Você não digitou uma das opções')