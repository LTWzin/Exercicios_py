frase = str(input('Digite uma frase: ')).lower().strip()
print('A letra "A" aparece {} vezes na frase descrita!'.format(frase.count('a')))
print('A primeira aparição da letra "A" ê na {}° letra!'.format(frase.find('a') + 1))
print('A letra "A" aparece pela ultima vez na possição {}'.format(frase.rfind('a')+ 1))
