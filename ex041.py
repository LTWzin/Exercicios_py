ano = int(input('Digite o ano de nascimento do atleta: '))
idade = 2023 - ano
if idade < 9:
    print('O atleta concorre a categoria Mirim!')
elif idade < 14:
    print('O atleta concorre a categoria Infantil!')
elif idade < 19:
    print('O atleta concorre a categoria Junior!')
elif idade < 22:
    print('O atleta concorre a categoria Sênior!')
else:
    print('O atleta concorre a categoria Master!')
    