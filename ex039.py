ano = int(input('Digite o seu ano de nascimento: '))
idade = (2023 - ano)
if idade < 18:
    print('Você deverá se apresentar em {} anos!'.format(18 - idade))
elif idade > 18:
    print('Você deveria ter se apresentado a {} anos!'.format(idade - 18))
else:
    print('Você deve se apresentar esse ano!')
