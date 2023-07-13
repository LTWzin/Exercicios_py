n = int(input('Digite um numero para fatorar: '))
fat = 1
while n-1 != 0:
    fat *= n
    n -= 1
print('O resultado é {}'.format(fat))