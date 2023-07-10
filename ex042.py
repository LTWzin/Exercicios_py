n1 = int(input('Digite o valor da maior linha: '))
n2 = int(input('Digite o valor da menor linha: '))
n3 = int(input('Digite o valor da linha restante: '))
if max(n1, n2, n3) != n1 or min(n1, n2, n3) != n2:
    print('Digite os valores corretamente!')
if n2 + n3 < n1:
    print('Não é possivel fazer um triangulo com essas 3 retas!')
elif n1 == n2 and n3:
    print('É possivel fazer um triangulo, ele seria um triangulo equilátero!')
elif n1 == n2 and n2 != n3 or n1 == n3 and n2 != n3 or n1 != n2 and n2 == n3:
    print('É possivel fazer um triangulo, ele seria um triangulo isósceles!')
elif n1 != n2 and n2 != n3:
    print('É possivel fazer um triangulo, ele seria um triangulo escaleno!')
