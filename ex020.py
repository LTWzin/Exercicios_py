from random import shuffle
a1 = str(input('Digite o nome do primeiro grupo: '))
a2 = str(input('Digite o nome do segundo grupo: '))
a3 = str(input('Digite o nome do terceiro grupo: '))
a4 = str(input('Digite o nome do quarto grupo: '))
grupos = [a1, a2, a3, a4]
shuffle(grupos)
print(grupos)
