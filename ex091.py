from random import randint
from time import sleep
from operator import itemgetter
rank = list()
jogadores = {'jogador 1': randint(1, 6),
             'jogador 2': randint(1, 6),
             'jogador 3': randint(1, 6),
             'jogador 4': randint(1, 6)}
sleep(0.6)
print('Os resultados foram sorteados.')
for c, v in jogadores.items():
    print(f'O {c} tirou: {v}')
    sleep(0.5)
print('-=' * 19)
sleep(0.8)
rank = sorted(jogadores.items(), key= itemgetter(1), reverse=True)
for indice, item in enumerate(rank):
    print(f'EM {indice + 1}º LUGAR: {item[0]} COM {item[1]}')
    sleep(0.5)
