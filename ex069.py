masculino = 0
feminino = 0 
maioridade = 0
while True:
    sexo = str(input('Digite o genero da pessoa [M/F] (Digite "q" para sair): ')).upper()
    if sexo == 'M':
        masculino += 1
    elif sexo == 'F':
        feminino += 1
    elif sexo == 'Q':
        break
    else: 
        print('Digite um genero existente!')
        break
    idade = int(input('Digite sua idade (Digite um numero negativo para terminar): '))
    if idade >= 18:
        maioridade += 1
    elif idade < 0: 
        break
print(
    f'Existem {masculino} homen(S) entre as pessoas digitadas e {feminino} mulher(es). Entre os participantes, {maioridade} eram maiores de idade!'
      )
