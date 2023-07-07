num = str(input('Digite um numero de 0 a 9999: '))
if num[0]:
    print('Unidade: {}'.format(num[0]))
elif num[1]:
    print('Dezena: {}'.format(num[1]))
elif num[2]:
    print('Centena: {}'.format(num[2]))
elif num[3]:
    print('Milhar: {}'.format(num[3]))
