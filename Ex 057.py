s = str('')
while s != 'F' and s != 'M':
    s = str(input('Qual o seu sexo? [F] ou [M]: ')).strip().upper()
    if s != 'F' and s != 'M':
        print('\033[31mInsira uma das opções válidas!\033[m')
print('\033[032mSexo {} registrado com sucesso\033[m!'.format(s))