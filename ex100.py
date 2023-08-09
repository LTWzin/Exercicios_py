#Desafio: Fazer programa com 2 funções e 2 lista!
from random import randint
numeros = []
pares = []

def sorteia(*ns):
    ns = randint(1, 10)
    numeros.append(ns)
    ns = randint(0, 10)
    numeros.append(ns)
    ns = randint(0, 10)
    numeros.append(ns)
    ns = randint(0, 10)
    numeros.append(ns)
    ns = randint(0, 10)
    numeros.append(ns)
    print('-=' * 19)
    print(f'Os 5 numeros sorteados foram {numeros}')
def somapar():
    somapares = 0
    for num in numeros:
        if num % 2 == 0:
            somapares += num
    print(f'Na soma de todos os numeros pares em {numeros}, o total é {somapares}')
    print('-=' * 19)


sorteia()
somapar()