from random import randint
numeros = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(f'Os numeros escolhidos foram: {numeros[0]} {numeros[1]} {numeros[2]} {numeros[3]} {numeros[4]}')
print(f'O MENOR numero foi {min(numeros)} e o MAIOR foi {max(numeros)}')