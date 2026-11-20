n = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('-'*30)
print('\033[035mPrograma tabuada encerrado. Volte sempre!\033[m')