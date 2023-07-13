while True:
    v1 = int(input('Digite um valor inteiro: '))
    v2 = int(input('Digite outro valor inteiro: '))
    op = int(input('''Digite o que fazer com esses numeros:
               [ 1 ] SOMA
               [ 2 ] MULTIPLICAR
               [ 3 ] SABER O MAIOR
               [ 4 ] ESCOLHER NOVOS NUMEROS
               [ 5 ] SAIR DO PROGRAMA
               -'''))
    if op == 1:
        print('A soma de {} com {} é igual a {}'.format(v1, v2, v1 + v2))
    if op == 2:
        print('O produto de {} por {} é {}'.format(v1, v2, v1 * v2))
    if op == 3:
        print('O maior numero entre {} e {} é {}'.format(v1, v2, max(v1, v2)))
    if op == 5:
        break
