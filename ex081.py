numeros = []
while True:
    num = int(input('Digite um numero: '))
    numeros.append(num)
    resp = str(input('Quer continuar? [S/N]  ')).upper()
    if resp  == 'N':
        break
numeros.sort(reverse= True)   #Ordenar em ordem decrescente
print('-=' * 13)
print(f'Foram digitados {len(numeros)} numeros')   #Quantia de numeros digitados
print(f'Os valores em ordem decrescente foram: {numeros}')
if 5 in numeros:   #Se o 5 está na lista
    print('O valor "5" está na lista na posição {}'.format(numeros.index(5) + 1))
else:
    print('O numero "5" não foi digitado!')