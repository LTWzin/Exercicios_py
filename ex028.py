import random
cpu = random.randint(1, 5)
print('A maquina eacolheu um numero aleatório!')
pessoa = int(input('Tente advinhar o numero de 1 a 5: '))
if pessoa == cpu:
    print('Você acertou! o numero é {}'.format(cpu))
    print('PARABÉNS!')
else:
    print('Você errou, o numero era {}'.format(cpu))
    