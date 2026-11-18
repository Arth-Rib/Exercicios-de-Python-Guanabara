escolha = 'S'
maior = 0
menor = 0
c = 0
soma = 0
while escolha != 'N':
    n = int(input('Digite o valor que deseja somar: '))
    escolha = str(input('Quer continuar? [S/N] ')).upper().strip()
    while escolha not in ['S', 'N']:
        print('Você não digitou uma opção válida, tente novamente.')
        escolha = str(input('Quer continuar? [S/N] ')).upper().strip()
    c += 1
    soma += n
    if c == 1:
        maior = menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
media = soma / c
print('Você digitou {} números.\nA média entre eles é {}.\nO maior número é {}.\nO menor número é {}.'.format(c, media, maior, menor))