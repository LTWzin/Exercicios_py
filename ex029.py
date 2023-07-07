velocidade = int(input('Digite a velocidade do carro em km/h: '))
multa = velocidade - 80
if velocidade > 80:
    print('Você foi mutado no valor de R${:.2f}'.format(multa * 8))
else:
    print('Tudo safe!')
    