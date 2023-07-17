compras = ('mouse', 29.90,
            'teclado', 44.90,
              'mesa digitalizadora', 145.00,
                'mousepad', 33.46,
                'ssd', 159.00,
                'led rgb', 29.00,
                'headset', 189.90,
                'kit limpeza para perifericos', 45.00
)
for item in range(0, len(compras)):
    if item % 2 == 0:
        print(f'{compras[item].title():.<30}', end= '')
    else:
        print(f'R$ {compras[item]:>6.2f}')