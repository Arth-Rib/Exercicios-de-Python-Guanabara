mh = 0
nv = 0
soma = 0
m20 = 0
for c in range(1, 5):
    n = str(input('Insira o nome da pessoa:'))
    i = int(input('Insira a idade:'))
    print('[F] para feminino\n[M] para masculino')
    s = str(input('Insira o sexo:')).upper()
    soma += i
    if s == 'M' and i > mh:
        mh = i
        nv = n
    if s == 'F' and i < 20:
        m20 += 1
media = soma / 4
print('A média de idade do grupo é {}.\nO homem mais velho se chama {}.\nTem {} mulhere(s) com menos de 20 anos.'.format(media, nv, m20))