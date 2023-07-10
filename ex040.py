n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('\033[31mREPROVADO!\033[m')
elif m < 6.9:
    print('\033[33mRECUPERAÇÃO!\033[m')
else:
    print('\033[32mAPROVADO!\033[m')
