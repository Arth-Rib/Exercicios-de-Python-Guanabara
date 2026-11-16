vc = float(input('Digite o valor da casa:'))
sc = float(input('Digite o valor do salario:'))
qp = int(input('Digite em quantos anos o pagamento:'))
parcela = vc/(qp*12)
if parcela <= (sc*0.3):
    print('Empréstimo aprovado!Sua parcela fica {} por mês.'.format(parcela))
else:
    print('Empréstimo negado!')