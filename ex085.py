numeros = [[], []]
atual = 1
for c in range(0, 7):
    numero = int(input(f'Digite o seu {atual}º numero:  '))
    atual += 1
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)
numeros[0].sort()
numeros[1].sort()
print(f'Os numeros impares foram {numeros[0]}\nOs numeros pares foram {numeros[1]}')
