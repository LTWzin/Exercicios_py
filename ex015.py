dias = int(input('Digite a quantia de dias rodados: '))
km = float(input('Digite a quantia de quilometros rodados: '))
precod = dias * 60
precokm = km * 0.15
preco = precod + precokm
print(
    '\nO preço pelo aluguel por {} dias e {} quilometros rodados é igual a R${:.2f}!'.format(dias, km, preco)
)
