pv = int(input('Digite o primeiro valor:'))
ps = int(input('Digite o segundo valor:'))
if pv > ps:
    print('O primeiro valor é maior.')
elif pv < ps:
    print('O segundo valor é maior.')
elif pv == ps:
    print('Não existe valor maior, ambos são iguais.')