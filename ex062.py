on = True
while on == True:
    n =int(input('Digite um numero inteiro: '))
    c = int(input('Em uma contagem, digite até que valor vai o seu numero: '))
    p = int(input('Pulando de quantos em quantos numeros: '))
    while n < c:
        print(n)
        n += p
