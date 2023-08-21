def leiaint(quest):
    while True:
        vern = input(quest)
        if vern.isnumeric():
            return vern
        else:
            print('\033[1;31mERROR! Digite um numero inteiro valido.\033[m')


n = leiaint('Digite um numero inteiro:  ')
print(f'Você digitou o numero inteiro "{n}".')