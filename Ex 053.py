f = str(input('Digite uma frase: ')).strip().upper().split()
s = ''.join(f)
r = s[::-1]
if s == r:
    print('É um palindromo.')
else:
    print('Não é um palindromo.')