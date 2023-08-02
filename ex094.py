pessoa = {}
todos = []
somaidades = 0
while True:
     nome = str(input('Digite o nome da pessoa:  ')).title()
     idade = int(input('Digite a idade da pessoa:  '))
     somaidades += idade
     sexo = str(input('Digite o sexo da pessoa [M/F]:  ')).upper()
     continuar = str(input('Quer continuar? [S/N]  ')).upper()
     pessoa['nome'] = nome
     pessoa['idade'] = idade
     pessoa['sexo'] = sexo
     todos.append(pessoa.copy())
     if continuar == 'N':
          break
print(f'Ao todo temos {len(todos)} pessoas cadastradas!')
print(f'A media das idades das pessoas cadastradas é de {somaidades / len(todos):.2f}')
print('As mulheres cadastradas foram: ', end= '')
for p in todos:
     if p['sexo'] == 'F':
          print(f'{p["nome"]}', end= ' ')
print()
print('-=' * 30)
print('Estão com a idade acima da media:  ', end= '')
for p in todos:
     if p['idade'] > somaidades / len(todos):
          print(f'{p["nome"]}', end= ' ')
          
