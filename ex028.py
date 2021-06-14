from random import randint
from time import sleep
pc = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar qual...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1.5)
print('')
if jogador == pc:
    print('PARABÉNS!! Você conseguiu me vencer dessa vez!')
else:
    print('GANHEI HAHAHA! Eu pensei no número {} e não no {}!'.format(pc, jogador))
