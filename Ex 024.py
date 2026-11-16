nome = str(input('Digite o nome da sua cidade: '))
up = nome.upper()
if up.find('SANTO')== 0:
    print('Sua cidade começa com Santo')
else:
    print('Sua cidade não começa com Santo')