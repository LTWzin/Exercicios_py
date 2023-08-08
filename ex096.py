def terreno(x, y):
    print(f'O seu terreno de {x} por {y} tem {x * y} metros quadrados (m²)')
def linha():
    print('-' * 17)


print('Controle de Terrenos')
linha()
a = float(input('Digite a largura (m) do seu terreno:  '))
b = float(input('Digite o comprimento (m) do seu terreno:  '))

terreno(a, b)
