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
