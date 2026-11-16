v = int(input('Digite a sua velocidade: '))
if v > 80:
    print('Você foi multado no valor de R${}'.format((v-80)*7))
else:
    print('Sem problemas.')