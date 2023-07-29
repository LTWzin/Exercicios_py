dados = {}
dados['nome'] = input('Digite o nome do aluno:  ').title().strip()
dados['media'] = float(input(f'Digite a media de {dados["nome"]}:  '))
if dados['media'] <= 6.9:
    dados['status'] = 'Reprovado'
else:
    dados['status'] = 'Aprovado'
for k, v in dados.items():
    print(f'{k}: {v}')
