p = float(input('Digite o seu peso em quilos: '))
a = float(input('Digite o seu altura em metros: '))
imc = p/(a*a)
if imc < 18.5:
    print('Seu IMC é {:.2f}, você está abaixo do peso!'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é {:.2f}, você está no peso ideal!'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é {:.2f}, você está com sobrepeso!'.format(imc))
elif imc >= 30 and imc <= 40:
    print('Seu IMC é {:.2f}, você está com obesidade!'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.2f}, você está com obesidade mórbida!'.format(imc))
