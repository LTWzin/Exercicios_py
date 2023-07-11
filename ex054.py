mi = 0 #maior idade
me = 0 #menor idade
for pessoas in range(0, 5):
    n = int(input('digite o ano do nascimento:'))
    i = 2023 - n
    if i > 21:
        mi += 1
    else:
        me += 1
print('Existe(m) {} pessoa(s) maior(es) de idade e {} menor(es)!'.format(mi, me))