n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('Média {:.2f}, \033[31m reprovado \033[m.'.format(m))
elif m >= 5 and m <= 6.9:
    print('Média {:.2f}, \033[35m recuperação \033[m.'.format(m))
elif m >= 7:
    print('Média {}, \033[32m aprovado \033[m.'.format(m))