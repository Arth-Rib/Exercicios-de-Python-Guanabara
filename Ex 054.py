import datetime
maior = 0
menor = 0
for c in range(1,8):
    a = int(input('Digite o ano de nascimento: '))
    if 18 <= datetime.date.today().year - a:
        maior += 1
    elif datetime.date.today().year - a < 18:
        menor += 1
print('Temos {} maiores de idade e {} menores de idade.'.format(maior, menor))