gen = input('Digite seu genero [M/F]: ')
while gen != 'M' and gen != 'F':
    gen = input('Argumento invalido. Tente novament [M/F]: ')
if gen == 'F':
    print('Genero valido. Entrando como "FEMININO".')
else:
    print('Genero valido. Entrando como "MASCULINO"')
