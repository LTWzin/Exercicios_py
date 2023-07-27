from time import sleep
numero = int(input('Digite até onde vai a contegem (segundos):  '))
for num in range(numero, 0, -1):
    print(f'~ \033[33m{num}\033[m')
    sleep(1)
print('Fim da contagem regressiva')