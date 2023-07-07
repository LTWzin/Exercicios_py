salario = float(input('Digite o seu salário: '))
if salario > 1300:
    print('Seu novo salário é de R${:.2f}'.format(salario * 1.10))
else:
    print('Seu novo salário é de R${:.2f}'.format(salario * 1.15))
    