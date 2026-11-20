# Meu Código
n = int(input('Digite um número que deseja saber o fatorial:'))
t= n-1
f = n*t
while t != 1:
    t = t-1
    f = f*t

print('O fatorial do número é {}'.format(f))

#Codigo do curso em video 1
'''from math import factorial
n = int(input('Digite o numero para calcular o fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n,f)))'''

# Codigo do curso em video 2
'''n = int(input('Digite o numero para calcular o fatorial:'))
c = n
while c > 0:
    print('{} '.format(c), end='')
    print(' x 'if c > 1 else '=', end='')
    f = f*c
    c -= 1
print('{}'.format(f))'''