frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
juntada = ''.join(palavra)
contrario = juntada[ : :-1]
print('{} {}'.format(juntada, contrario))
if contrario == juntada:
    print('É um palindromo!')
else:
    print('Não é um palindromo!')
