classificacao = (
    'Botafogo', 'Flamengo', 'Gremio', 'São Paulo', 'Fluminense', 'Palmeiras',
    'Bragantino', 'Athletico-PR', 'Fortaleza', 'Cruzeiro', 'Internacional',
    'Atletico-MG', 'Cuiaba', 'Santos', 'Corinthians', 'Bahia', 'Goias', 'Coritiba',
    'Vasco da Gama', 'America-MG'
)   #Classificação do Brasileirão do dia 17/07/2023. Rodada 15.
tabela = 1
ultimos = -1
for colocado in range (0, 5):   #Primeiros colocados
    print(f'{tabela}- {classificacao[colocado]}')
    tabela += 1 
tabela = 20
print('-' * 13)
for colocado2 in range (0, 4):   #Ultimos colocados
    print(f'{tabela}- {classificacao[ultimos]}')
    tabela -= 1
    ultimos -= 1
print('-' * 13)
print(sorted(classificacao))   #Organizar em ordem alfabética
print('-' * 13)
sp = classificacao.index('São Paulo')   #Classificação do 'São Paulo na tupla
print('O São Paulo está na possição {} da tabela'.format(sp + 1))