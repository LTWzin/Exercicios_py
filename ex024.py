city = str(input('Digite um nome de uma cidade: '))
city = city.lower()
if 'santo' in city:
    print('Existe a palavra "Santo(a)" na cidade escolhida')
elif 'santa' in city:
    print('Existe a palavra "Santo(a)" na cidade escolhida')
else:
    print('Não existe a palavra "Santo(a) na cidade escolhida')