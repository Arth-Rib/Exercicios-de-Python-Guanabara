# Minha solução
pt = float(input('Digite o primeiro termo da PA: '))
rz = float(input('Digite a razao: '))
lista = []
lista.append(pt)
c = 0
while c < 10:
    while c != 9:
        lista.append(rz+pt)
        pt += rz
        c += 1
    print('Os termos são: \n{}'.format(lista))
    print('-------//-------')
    s = int(input('Mais quantos termos deseja: '))
    if c != 0:
        c -= s
    if s == 0:
        c = 10
print('FIM')

#Solução do Curso
''''''