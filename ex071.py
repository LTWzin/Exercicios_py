c50 = 0   #CEDULAS DE 50
c20 = 0   #CEDULAS DE 20
c10 = 0   #CEDULAS DE 10
c1 = 0    #CEDULAS DE 01
print('-=' * 13)
valor = int(input('Digite o valor a ser sacado: '))
print('-=' * 13)
while valor > 50:
    valor -= 50
    c50 += 1
while valor > 20:
    valor -= 20
    c20 += 1
while valor > 10:
    valor -= 10
    c10 += 1
while valor >= 1:
    valor -= 1
    c1 += 1
if c50 != 0:
    print(f'ENTREGUE {c50} CEDULA(S) DE R$50')
if c20 != 0:
    print(f'ENTREGUE {c20} CEDULA(s) DE R$20')
if c10 != 0:
    print(f'ENTREGUE {c10} CEDULA(S) DE R$10')
if c1 != 0:
    print(f'ENTREGUE {c1} CEDULA(S) DE R$1')
    