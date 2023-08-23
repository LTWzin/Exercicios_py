from conteudos107 import moeda

nn = int(input('Digite o valor do preço:  R$'))
print(f'O dobro de {nn} é {moeda.dobro(nn)}')
print(f'A metade de {nn} é {moeda.metade(nn)}')
print(f'Almentando 20% de {nn}, temos {moeda.aumento(nn, 20)}')
print(f'Reduzindo 26% de {nn}, temos {moeda.reducao(nn, 26)}')
