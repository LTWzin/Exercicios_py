v1 = input('Digite algo:\n')
print('\nDe que tipo? ', type(v1))
print('É um numero? ', v1.isnumeric())
print('É uma letra? ', v1.isalpha())
print('Numero e/ou letra?', v1.isalnum())
print('Maiuscula? ', v1.isupper())
print('Minuscula? ', v1.islower())
print('Titulo? ', v1.istitle())