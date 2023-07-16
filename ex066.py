numero = 0
quantidade = 0 
soma = 0
while True:
    numero = int(input('Digite um número (digite 999 para parar): '))
    if numero == 999:
        break
    quantidade += 1
    soma += numero
print(f'A soma dos numeros é de {soma} e a quantia de números digitados é de {quantidade}!')