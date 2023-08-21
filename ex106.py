'''Sistema help() do python'''
print('-=' * 12)
print(' Sistema de ajuda PyHelp')
print('-=' * 12)
while True:
    func = str(input('\033[34mFunção ou biblioteca\033[m > '))
    if func == 'fim':
        break
    else:
        print(f'{help(func)}\n')
print('\033[35;44mFim do Programa!\033[m')