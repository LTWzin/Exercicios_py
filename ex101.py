def voto(nascimento):
    idade = 2023 - nascimento
    if idade >= 18 and idade <= 65:
        return 'Voto Obrigatório!'
    elif idade < 18 and idade >= 16:
        return 'Voto Opicional!'
    elif idade > 65:
        return 'Voto Opicional!'
    else:
        return 'Voto Negado!'
    

idade = int(input('Digite o ano do seu nascimento:  '))
print('-=' * 19)
print(f'Com {2023 - idade} anos você tem {voto(idade)}')
