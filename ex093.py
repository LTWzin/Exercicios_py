jogador = {}
gols = []
totalgol = 0
partida = 1
nome = str(input('Digite o nome do jogador:  ')).title()
quantia = int(input(f'Quantas partidas {nome} jogou:  '))
jogador['nome'] = nome
for cont in range(0, quantia):
    gol = int(input(f'Quantos gols {jogador["nome"]} fez na partida {cont + 1}:  '))
    gols.append(gol)
    totalgol += gol
jogador['score'] = gols
jogador['total'] = totalgol
print('-=' * 17)
print(jogador)
print('-=' * 17)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('-=' * 17)
print(f'{jogador["nome"]} fez {jogador["total"]} gols em {quantia} partidas')
for p in jogador['score']:
    print(f'    => Na partida {partida} ele fez {p} gols!')
    partida += 1