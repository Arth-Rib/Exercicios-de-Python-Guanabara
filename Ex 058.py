import random
print('\033[4:36mTente adivinhar o número que estou pensando de 1 a 10!\033[m')
c = random.randint(1,10)
cont = 0
j = 0
while j != c:
    j = int(input('Digite o seu chute: '))
    cont += 1
    if j != c:
        print('\033[031mErrou, tente novamente!\033[m')
print('\033[032mAcertou! Você ganhou em {} tentativas!\033[m'.format(cont))