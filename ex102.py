def fatorial(num=1, show=False):
    a = 1
    if show == False:  # Sem Mostrar a multiplicao
        while num != 1:
            a *= num
            num -= 1
        return a
    else:  # Mostrando a multiplicao
        while num != 1:
            print(f'{num} x ', end= '')
            a *= num
            num -= 1
        print('1 = ', end= '')
        return a


print('-' * 38)
numero = int(input('Digite um numero para fatorar:  '))
print('-=' * 19)
print(fatorial(numero, show=True))