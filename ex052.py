p = 0
num = int(input('Digite um numero: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end= '')
        p += 1
    else:
        print('\033[m', end= '')
    print('{} '.format(c), end= '')
print('\033[m\nO numero {} foi divisivel {} vezes.'.format(num, p))
if p == 2:
    print('Ele é um número primo!')
    