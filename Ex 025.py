nome = str(input('Digite seu nome completo: ')).strip()
up = nome.upper()
if up.find('SILVA') != -1:
    print('Seu nome tem Silva')
else:
    print('Seu nome não tem Silva')