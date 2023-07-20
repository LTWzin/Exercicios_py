allnumeros = []
impares = []
pares = []
while True:
    num = int(input('Digite um numero: '))
    allnumeros.append(num)
    if allnumeros[-1] % 2 == 0:
        pares.append(allnumeros[-1])
        allnumeros.pop()
    else:
        impares.append(allnumeros[-1])
        allnumeros.pop()
    resp = str(input('Quer continuar? [S/N]  ')).upper()
    if resp == 'N':
        break
    print('-=' * 13)
print(f'Os numeros digitados foram: {allnumeros}')    
print(f'Numeros impares: {impares}\nNumeros pares: {pares}')

