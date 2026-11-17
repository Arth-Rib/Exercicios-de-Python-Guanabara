n = int(input('Digite o úmero que deseja saber se é primo: '))
s = 0
for c in range(1,n+1):
    if n % c == 0:
        s += 1
if s == 2:
    print('Ele é primo!')
else:
    print('Não é primo!')