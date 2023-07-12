homemvelho = ''
idadevelho = 0
midade = 0
mulheres = 0
for nump in range(1, 4):
    print('-=-=-=- {}a Pessoa -=-=-=-'.format(nump))
    nome = str(input('NOME: ')).title().strip()
    genero = str(input('GENERO (M/F): '))
    idade = int(input('IDADE: '))
    midade += idade
    if nump == 1 and genero in 'Mm':
       homemvelho = nome
       idadevelho = idade 
    if genero in 'Mm' and idade > idadevelho:
        idadevelho = idade
        homemvelho = nome
    if genero in 'Ff' and idade < 20:
        mulheres += 1
print('A media de idade do grupo é de {:.2f}'.format(midade / 3))
print('O nome do homem mais velho é {} com {} anos.'.format(homemvelho, idadevelho))
print('{} Mulher(es) tem menos de 20 anos!'.format(mulheres))
 