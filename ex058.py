tentativas = 0
import random
cpu = random.randint(1, 10)
print('\033[34mA maquina escolheu um numero aleatório!')
pessoa = int(input('Tente advinhar o numero de 1 a 10:\033[m '))
while pessoa != cpu:
    pessoa = int(input('\033[31mResposta errada\033[m. Tente novamente: '))
    tentativas += 1
print('\033[32mVOCÊ ACERTOU!\033[m\nVocê tentou {} vezes antes de acertar!'.format(tentativas))
