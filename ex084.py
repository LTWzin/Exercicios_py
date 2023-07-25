geral = list()
pessoa = list()
cadastrados = totmai = totmen = 0
while True:
    cadastrados += 1
    pessoa.append(str(input('Digite o nome da pessoa:  ')).title().strip())
    pessoa.append(int(input('Digite o peso da pessoa:  ')))
    geral.append(pessoa[:])
    pessoa.clear()
    continuar = str(input('Quer continuar? [S/N]   ')).upper().strip()
    if continuar == 'N':
        break
print('No total foram cadastrados {} nomes.'.format(cadastrados))
print('Os que tiveram mais que 100KG foram: ', end= '')
for pess in geral:
    if pess[1] >= 100:
        totmai += 1
        print(pess[0], end= ' ')
if totmai == 0:
    print('ninguem!', end= '')
print('\n', end= '')
print('Os que pesam menos de 70KG são:  ', end= '')
for pes in geral:
    if pes[1] <= 70:
        totmen += 1
        print(pes[0], end= ' ')
if totmen == 0:
    print('ninguem!')
