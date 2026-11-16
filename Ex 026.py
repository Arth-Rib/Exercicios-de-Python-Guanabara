frase = str(input('Digite uma frase: ')).upper()
print('Sua frase tem {} letras "A".'.format(frase.count('A')))
print('A primeira posição de "A" é: {}'.format(frase.find('A')+1))
print('A ultima posição de "A" é: {}'.format(frase.rfind('A')+1))
