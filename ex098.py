from operator import neg
from time import sleep

def sequencia(x, y, z):
    print(f'Contando de {x} a {y} de {z} em {z}')
    if x > y and z > 0:
        for num in range(x, y -1, neg(z)):
            print(num, end= ' ')
        print('Fim!')
    elif y > x and z > 0:
        for num in range(x, y + 1, z):
            print(num, end= ' ')
        print('Fim!')
    elif y > x and z < 0:
        for num in range(x, y + 1, abs(z)):
            print(num, end= ' ')
        print('Fim!')
    elif x > y and z < 0:
        for num in range(x, y -1, z):
            print(num, end= ' ')
        print('Fim!')
    elif x > y and z == 0:
        for num in range(x, y, -1):
            print(num, end= ' ')
        print('Fim!')
    elif y > x and z == 0:
        for num in range(x, y, 1):
            print(num, end= ' ')
        print('Fim!')


print('-=' * 13)
print(f'{"CONTAGEM":^26}')
print('-=' * 13)
sequencia(0, 10, 1)
print('~' * 27)
sequencia(10, 0, 2)
print('~' * 27)
print('SUA VEZ')
print('~' * 27)
inicio = int(input('Digite o numero inicial:  '))
fim = int(input('Digite o numero final:  '))
passo = int(input('De quanto em quanto:  '))
print('~' * 27)
sequencia(inicio, fim, passo)