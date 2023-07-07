l1 = int(input('Digite o tamanho da maior reta: '))
l2 = int(input('Agora digite o tamanho da menor reta: '))
l3 = int(input('Por ultimo, o tamanho da terceira reta: '))
if max(l1, l2, l3) != l1:
    print('Digite o valor corretamente!')
    exit()
if l2 + l3 < l1:
    print('Não é possivel fazer um triangulo com essas linhas')
else:
    print('É possivel fazer um triangulo, sua area é de {}m²/c²'.format(l2 + l1 + l3))