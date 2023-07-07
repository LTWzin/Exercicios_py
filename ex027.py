nome = str(input('Digite seu nome completo: ')).split()
print('prazer em conhecer \033[31;1m{}\033[m!'.format(nome[0].title()))
print('Seu ultimo nome é {}'.format(nome[-1].title()))
