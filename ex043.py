altura = float(input('Digite  a sua altura (em cm): '))
peso = float(input('Digite o seu peso (em kg): '))
IMC = peso / (altura / 100)**2
if IMC < 18.5:
    print('Abaixo do peso!')
elif IMC < 25:
    print('Peso ideal!')
elif IMC < 30:
    print('Sobrepeso!')
elif IMC < 40:
    print('Obesidade!')
else:
    print('Obesidade mórbida!')