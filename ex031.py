d = int(input('Digite a distancia da viagem em km²: '))
if d > 400:
    valor = d * 0.45
else:
    valor = d * 0.50
print('O valor da viagem fica a R${}'.format(valor
))