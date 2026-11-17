import datetime
a = int(input('Digite o ano de nascimento do atleta: '))
i = datetime.date.today().year - a
if i <= 9:
    print('Atleta mirim')
elif i <=14:
    print('Atleta infantil')
elif i <=19:
    print('Atleta junior')
elif i <=25:
    print('Atleta senior')
elif i > 25:
    print('Atleta master')