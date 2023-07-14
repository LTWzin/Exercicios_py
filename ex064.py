n = int(input('Digite um numero: ')) #numero
nd = 1 #numeros digitados
t = 0 #total
t += n #total mais numero
while n != 999: #999 condição de parada
    n = int(input('Digite um numero (Digite 999 para sair): '))
    t += n
    nd += 1
print('O total de numeros digitados foi de {} e a soma dos numeros foi de {}'.format(nd-1, t-999))
    