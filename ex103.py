def ficha(seminfo='<Não informado>', gols=0):
    print('-=' * 19)
    print(f'O jogador {seminfo} fez {gols} gol(s) no campeonato')


print('-=' * 19)
nome = input('Digite o nome do jogador:  ').strip().title()
gol = str(input('Digite a quantia de gols do jogador:  ')).strip()

if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0

if nome.strip() == '':
    ficha(gols=gol)
else:
    ficha(nome, gol)