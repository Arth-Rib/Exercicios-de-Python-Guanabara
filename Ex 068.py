import random
v = 0
while True:
    while True:
        escolha = str(input('[P] PAR\n[I] IMPAR\nEscolha par ou impar? ')).strip().upper()
        if escolha in 'PI':
            break
        print('Faça uma escolha de par ou impar! Digite [P] para par ou [I] para impar!')
        print('-'*30)
    j = int(input('Escolha o numero que deseja jogar: '))
    print('-'*30)
    c = random.randint(1, 1000)
    if escolha in 'P':
        if (j+c) % 2 == 0:
            v += 1
            print(f'Você jogou {j} e o computador jogou {c}.')
            print('Parabens! Voce ganhou!\nVamos jogar novamente...')
            print('=-'*30)
        elif (j+c) % 2 != 0:
            print(f'Você jogou {j} e o computador jogou {c}.')
            print('Voce perdeu!')
            break
    print('=-' * 30)
    elif escolha in 'I':
        if (j+c) % 2 == 0:
            print(f'Você jogou {j} e o computador jogou {c}.')
            print('Voce perdeu!')
            break
        elif (j+c) % 2 != 0:
            v += 1
            print(f'Você jogou {j} e o computador jogou {c}.')
            print('Parabens! Voce ganhou!\nVamos jogar novamente...')
    print('=-' * 30)
print(f'GAME OVER! Você venceu {v} vezes!')
