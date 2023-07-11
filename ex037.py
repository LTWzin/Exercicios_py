numero = int(input('Digite um numero inteiro: '))
obs = int(input('''Digite a opção desejada:
  [ 1 ] Transformar numero em BÍNARIO
  [ 2 ] Transformar numero em OCTAL
  [ 3 ] Transformar numero em HEXADECIMAL\n-'''))
if obs == 1:
    print('O numero {} em bínario é igual a {}'.format(numero, bin(numero) [2: ] ))
elif obs == 2:
    print('O número {} em octal é igual a {}'.format(numero, oct(numero) [2: ] ))
elif obs == 3:
    print('O número {} em hexadecimal é igual a {}'.format(numero, hex(numero) [2: ] ))
else:
    print('Opção invalida! Tente novamente.')
