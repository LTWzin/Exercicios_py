n =int(input('Digite um numero inteiro: '))
c = int(input('Em uma contagem, digite até que valor vai o seu numero: '))
p = int(input('Pulando de quantos em quantos numeros: '))
for num in range(n, c+1, p):
    print(num)