fatorial = 0
                    #Cor azul
print('''
                \033[34mTABUADA!\033[m     
      Digite um numero negativo para sair''')   
while True:   #Infinito
    numero = int(input('Digite um número: '))
    if numero <= 0:
        break   #Parar o codigo
    for result in range(0, numero * 11):   #Fatorias 
        if result % numero == 0:
            print(f'{numero} x {fatorial} = {result}')
            fatorial += 1
            if fatorial == 11:   #Recomeçar a tabuada
                fatorial = 0