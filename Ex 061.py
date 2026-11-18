pt = float(input('Digite o primeiro termo da PA: '))
rz = float(input('Digite a razao: '))
lista = []
lista.append(pt)
c=0
while c != 9:
    lista.append(rz+pt)
    pt += rz
    c += 1
print('Os termos são: \n{}'.format(lista))