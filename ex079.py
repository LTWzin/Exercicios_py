numeros = []   #Lista de numeros
numeros.append(int(input('Digite um numero: ')))
while True:   #Looping infinito
    numero = (int(input('Digite outro numero: ')))   
    if numero not in numeros:   #Verificar se o numero já está na lista
        numeros.append(numero)
    resposta = str(input('Quer continuar? [S/N] ')).upper()
    while resposta != 'S' and resposta != 'n' and resposta != 'N' and resposta != 's':
        resposta = str(input('Quer continuar? [S/N] ')).upper
        if resposta == 'N':
            break
    if resposta == 'N' or resposta == 'n':
        break
numeros.sort()
print('Você digitou os valores {}'.format(numeros))
