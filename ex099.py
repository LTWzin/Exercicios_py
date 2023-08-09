num = 0
def maior(*numeros):
    print('-=-=-=-=-=' + 'Analizando' + '-=-=-=-=-=')
    if len(numeros) == 0:
        print('Você não digitou nenhum numero')
    else:   
        print(f'Você digitou {len(numeros)} numeros')
        print(f'O maior numero dentre {numeros} é o {max(numeros)}')


maior(1, 4, 7, 2, 0)
maior(93, -1, 4, 7, 2, 27, 15)
        