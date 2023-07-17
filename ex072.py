numeros = (
    'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze'
)
numero = int(input('Digite um numero entre 0 e 13: '))
while not numero <= 0 and numero >= 13:
    numero = int(input('Tente novamente. Digite um numero entre 0 e 13: '))
print(numeros[numero].title())
