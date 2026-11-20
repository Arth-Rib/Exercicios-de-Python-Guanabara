print('=-'*30)
print('Banco CEV')
print('=-'*30)
v = int(input('Qual o calor que deseja sacar? R$ '))
cinq = v // 50
vinte = (v - cinq * 50) // 20
dez = ((v - cinq * 50) - vinte * 20) // 10
um = ((v - cinq * 50) - vinte * 20) % 10
print('-'*30)
if cinq > 0:
    print(f'Total de {cinq} cédulas de R$50')
if vinte > 0:
    print(f'Total de {vinte} cédulas de R$20')
if dez > 0:
    print(f'Total de {dez} de R$10')
if um > 0:
    print(f'Total de {um} de R$1')
print('=-'*30)
print('Volte sempre ao Banco CEV! Tenha um bom dia!')

#Resolução do curso em video
'''print('=-'*30)
print('Banco CEV')
print('=-'*30)
v = int(input('Qual o calor que deseja sacar? R$ '))
total = valor
céd = 50
totalced = 0
while True:
    if total >= céd:
        total -= céd
        totalced += 1
    else:
        if totalced > 0:
        print(f'Total de {totcéd} cédulas de {céd}')
        if total == 50:
            céd = 20
        elif total == 20:
            céd = 10
        elif total == 10:
            céd = 1
        totalced = 0
        if total == 0:
            break'''