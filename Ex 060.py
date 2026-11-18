n = int(input('Digite um número que deseja saber o fatorial:'))
t= n-1
f = n*t
while t != 1:
    t = t-1
    f = f*t

print('O fatorial do número é {}'.format(f))