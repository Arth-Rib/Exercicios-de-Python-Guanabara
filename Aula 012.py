nome = str(input('Qual o seu nome? '))
if nome == 'Arthur':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Isabela Ana Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem comum.')
print('Tenha um bom dia, {}!'.format(nome))