from math import sqrt
ca = float(input('Digite o valor do cateto adjacente: '))
co = float(input('Digite o valor do cateto oposto: '))
h = (ca**2 + co**2)
print('O valor da hipotenusa é {:.3f}'.format(sqrt(h)))