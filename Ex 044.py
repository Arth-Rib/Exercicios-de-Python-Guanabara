p = float(input('Digite o valor do produto em R$: '))
print('''Escolha uma forma de pagamento:''')
print('1 - a vista em dinheiro/cheque\n2 - a vista no cartão\n3 - em até 2x no cartão\n4 - 3x ou mais no cartão')
op = int(input('Digite uma das opções acima:'))
if op == 1:
    print('O valor a ser pago é R${:.2f}'.format(p*0.9))
elif op == 2:
    print('O valor a ser pago é R${:.2f}'.format(p*0.95))
elif op == 3:
    print('O valor a ser pago é R${:.2f}'.format(p))
elif op == 4:
    print('O valor a ser pago é R${:.2f}'.format(p*1.2))
else:
    print('Opção não existe! Reinicie o programa!')