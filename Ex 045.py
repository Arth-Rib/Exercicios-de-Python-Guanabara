import random
print('\033[4:31:47m--------JOKENPÔ--------\033[m')
print('Escolha uma das opções:')
print('[ 0 ] Pedra')
print('[ 1 ] Papel')
print('[ 2 ] Tesoura')
j1 = int(input('Digite sua escolha:'))
if j1 == 0:
    h=0
elif j1 == 1:
    h=1
elif j1 == 2:
    h=2
lista = [0,1,2]
c = random.choice(lista)
if c == 0 and j1 == 0 or c == 1 and j1 == 1 or c == 2 and j1 == 2:
    if c == 0:
        c = 'pedra'
    elif c == 1:
        c = 'papel'
    elif c == 2:
        c = 'tesoura'
    print('Eu escolhi {}, então temos um empate!'.format(c))
elif c == 1 and j1 == 0 or c==2 and j1 == 1 or c == 0 and j1 == 2:
    if c == 0:
        c = 'pedra'
    elif c == 1:
        c = 'papel'
    elif c == 2:
        c = 'tesoura'
    print('Eu escolhi {}, então eu ganhei!'.format(c))
elif c == 2 and j1 == 0 or c == 1 and j1 == 2 or c == 0 and j1 == 1:
    if c == 0:
        c = 'pedra'
    elif c == 1:
        c = 'papel'
    elif c == 2:
        c = 'tesoura'
    print('Eu escolhi {}, então você ganhou!'.format(c))
