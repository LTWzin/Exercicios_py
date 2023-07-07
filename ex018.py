import math
ang = int(input('Digite o angulo da circunferencia: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print('Valores do angulo {}:\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(ang, seno, cosseno, tangente))