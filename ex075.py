v1 = int(input())
v2 = int(input())
v3 = int(input())
v4 = int(input())
v5 = int(input())
tupla = (v1, v2, v3, v4, v5)
print(f'O valor "9" apareceu {tupla.count(9)} vezes')
print(f'O primeiro digito "3" aparece na posição {tupla.index(3) + 1}' if 3 in tupla else 'Não aparece "3" entre os digitos')
print('Os numeros pares que apareceram foram ', end= '')
for numero in tupla:
    if numero % 2 == 0:
        print(numero, end= ' ')
        