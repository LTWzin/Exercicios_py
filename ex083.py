expressao = str(input('Digite uma expressão matematica com parenteses: '))
sequencia = list()
for simbolo in expressao:
    if simbolo == '(':
        sequencia.append('(')
    elif simbolo == ')':
        if len(sequencia) > 0:
            sequencia.pop()
        else:
            sequencia.append(')')
            break
if len(sequencia) == 0:
    print('Sua expressão é valida! ')
else:
    print('Sua expressão está invalida! ')