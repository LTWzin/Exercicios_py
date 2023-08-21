def notas(*aluno, situacao=False):
    maior = 0
    menor = 0
    media = 0
    for nota in aluno:
        if maior == 0:
            maior = nota
        elif maior < nota:
            maior = nota
    for nota in aluno:
        if menor == 0:
            menor = nota
        elif menor > nota:
            menor = nota
    for nota in aluno:
        media += nota
    mediatotal = media / len(aluno)
    media = mediatotal
    print(f'''
Quantia de notas: {len(aluno)}
Maior nota: {maior}
Menor nota: {menor}
Media total: {media:.1f}''')
    if situacao == True:
        if media <= 6:
            print('A situação é RUIM.\n')
        elif media < 7:
            print('A situação é RAZOAVEL.\n')
        else:
            print('A situação é BOA.\n')


notas(9, 5, 7, 10, 6, situacao=True)
print('-=' * 13)
notas(5, 2, 9, 6, 8, 10, 7, 5, situacao=False)
