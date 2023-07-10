valor = float(input('Digite o valor da compra: '))
print('''1: A vista (10% de desconto)
2: No cartão de debito (5% de desconto)
3: No cartão de cretido 
4: No cartão em 2X (Acrecimo de 15%)''')
fp = float(input('Digite a forma de pagamento: '))
if fp == 1:
    print('Sua compra sai no valor de R${:.2f}'.format(valor - (0.10 * valor)))
elif fp == 2:
    print('Sua compra sai no valor de R${:.2f}'.format(valor - (0.05 * valor)))
elif fp == 3:
    print('Sua compra sai no valor de R${:.2f}'.format(valor))
elif fp == 4:
    print('Sua compra sai no valor de R${:.2f}'.format(valor + (0.15 * valor)))
else:
    print('Digite uma forma de pagamento valida!')