p = float(input('Digite o primeiro valor: '))
s = float(input('Digite o segundo valor: '))
t = float(input('Digite o terceiro valor: '))
l = [p,s,t]
if p > s and p > t:
    print('O maior valor é {}.'.format(p))
elif s > p and s > t:
    print('O maior valor é {}.'.format(s))
elif t > p and t > s:
    print('O maior valor é {}.'.format(t))
else:
    print('Você digitou valores iguais!')
if p < s and p < t:
    print('O menor valor é {}.'.format(p))
elif s < p and s < t:
    print('O menor valor é {}.'.format(s))
elif t < p and t < s:
    print('O menor valor é {}.'.format(t))
else:
    print('Você digitou valores iguais!')