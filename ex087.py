numeros = [[], [], []]   #Desafio: Matriz usando apenas uma lista!
numpar = 0
numesquerdo = numdireito = posicao = 0
print('-=' * 5)
print('| Matriz |')
print('-=' * 5)
for c in range(0, 9):   #Pergunta 9x
    num = int(input(f'Digite um valor para [{numesquerdo}, {numdireito}]:  '))
    if num % 2 == 0:
        numpar += num
    numeros[posicao].append(num)   #Guarda  o valor em uma das posiçoes da lista
    numdireito += 1
    if numdireito == 3:   #Onde o maximo de itens dentro da lista dentro da lista é 3
        numesquerdo += 1  #Com 3 listas para organização
        numdireito = 0
        posicao += 1
print('-=' * 13)   #MATRIZ
print(f'[ {numeros[0][0]} ] [ {numeros[0][1]} ] [ {numeros[0][2]} ]')
print(f'[ {numeros[1][0]} ] [ {numeros[1][1]} ] [ {numeros[1][2]} ]')
print(f'[ {numeros[2][0]} ] [ {numeros[2][1]} ] [ {numeros[2][2]} ]')
print(f'O MAIOR numero da segunda linha é: {max(numeros[1])}')
soma3 = numeros[0][2] + numeros[1][2] + numeros[2][2]
print(f'A soma dos valores da terceira coluna é: {soma3}')
print(f'O valor da soma de todos os numeros pares são: {numpar}')