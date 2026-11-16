r1 = float(input('Digite o segmento da primeira reta: '))
r2 = float(input('Digite o segmento da segunda reta: '))
r3 = float(input('Digite o segmento da segunda reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('É possível fazer um triangulo com esses segmentos!')
else:
    print('Não é possivel fazer um triângulo com esses segmentos!')
