n = int(input('Digite o numero que deseja ver a tabuada: '))
for c in range(1,11):
    print('{} x {:2} = {}'.format(n,c,c*n))