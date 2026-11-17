r1 = float(input('Digite o segmento da primeira reta: '))
r2 = float(input('Digite o segmento da segunda reta: '))
r3 = float(input('Digite o segmento da segunda reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('É possível fazer um triangulo com esses segmentos!')
    if r1 == r2 == r3:
        print('Forma um trinagulo equilátero.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Forma um triângulo isósceles.')
    elif r1 != r2 != r3 != r1:
        print('Forma um triângulo escaleno.')
    else:
        print('Erro')
else:
    print('Não é possivel fazer um triângulo com esses segmentos!')
