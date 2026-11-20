mmil = barato = soma = 0
menor = ''
while True:
    n = str(input('Nome do produto: ')).strip()
    p = int(input('Preço: R$ '))
    print('-' * 30)
    soma += p
    if p > 1000:
        mmil += 1
    if barato == 0 or p < barato:
        barato = p
        menor = n
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
print('-' * 15, 'FIM DO PROGRAMA','-' * 15)
print(f'O total da compra foi de R${soma:.2f}')
print(f'Temos {mmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {menor} por R${barato}.')