pt = float(input('Digite o primeiro termo da PA: '))
rz = float(input('Digite a razao: '))
lista = []
lista.append(pt)
for c in range(1,10):
    lista.append(pt+rz)
    pt += rz
print(lista)