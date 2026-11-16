d = int(input('Qual será a distância da viagem? '))
if d <= 200:
    print('O valor da passagem deveria ser de R${:.2f}'.format(d*0.5))
else:
    print('O valor da passagem deveria ser de R${:.2f}'.format(d*0.45))