import datetime
a = int(input('Digite o seu ano de nascimento: '))
i = datetime.date.today().year - a
if i > 18:
    print('Já passou {} ano(s) do seu alistamento.'.format(i-18))
elif i == 18:
    print('Está na hora de se alistar.')
elif i < 18:
    print('Você ainda vai precisar se alistar futuramente, em {} ano(s).'.format(18-i))
