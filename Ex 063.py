n = int(input('Digite quantos termos deseja ver da Sequência de Fibonacci: '))
c = 0
i = 0
e = 0
s = 0
lista = []
while c < n:
    s = i + e
    c += 1
    lista.append(s)
    if i == 0:
        i += 1
    if c == 3:
        e += 1
    if e > 0:
        i = e
        e = s
print(lista)

#Solução do Curso em Video
'''print('-'*40)
print('Sequencia de Fibonacci')
print('-'*40)
n = int(input('Digite quantos termos deseja ver: '))
t1 = 0
t2 = 1
print('~'*40)
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('-> {}'.format(t3), end='')
    cont += 1
    t1 = t2
    t2 = t3
print('-> FIM')'''
