t = 0
tp = 0
for num in range(0, 6):
    n = int(input('Digite um valor: '))
    t += n
    if n % 2 == 0:
        tp += n
print('A soma de todos os valores é {}\nA soma de todos os valores pares é igual a {}.'.format(t, tp))
