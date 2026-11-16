import random
print('Vou pensar em um numero entre 1 e 5')
c = int(input('Tente adivinhar: '))
r = random.randint(1,5)
print('O numero escolhido foi {}'.format(r))
if c == r:
    print('Parabéns! Você acertou!')
else:
    print('Não foi dessa vez! Tente novamente na próxima')

