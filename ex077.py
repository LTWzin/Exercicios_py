palavras = ('cabeça', 'urso', 'sexta', 'germany', 'estrapolado', 'escova'
             'futuro', 'dezembro', 'salsa', 'pneumoultramicroscopicossilicovulcanoconiótico')
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} tem as vogais ', end= '')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')