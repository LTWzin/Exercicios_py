menor = 0   #menor valor
posmenor = 0   #posição do menor valor
maior = 0   #maior valor
posmaior = 0   #posição do maior valor
numeros = []
for pergunta in range(0, 5):   #Pergunta 5 vezes
    numeros.append(int(input('Digite um valor: ')))   #Adiciona a lista
    for posicao, valor in enumerate(numeros):   #Posição e valor do numero digitado
        if menor == 0:   #Achar o menor valor
            menor = valor
            posmenor = posicao
        elif valor < menor:
            menor = valor
            posmenor = posicao
        if valor > maior:   #Achar o maior valor
            maior = valor
            posmaior = posicao
print(
    f'O MENOR valor foi {menor} na posição {posmenor + 1} e o Maior valor foi {maior} na posição {posmaior + 1}')