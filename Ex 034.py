s = float(input('Digite seu salario: '))
print('Seu salário aumentará para R${:.2f}'.format(s * 1.10) if s > 1250 else 'Seu salário aumentará para R${:13.2f}'.format(s * 1.15))