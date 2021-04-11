# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O Programa deverá escrever na tela se o usuário venceu ou
# perdeu

from random import randrange
numPC = randrange(6)
print('O computador escolheu um número entre 0 e 5.')
numUser = int(input('Qual número você acha que o computador escolheu? '))

if numUser == numPC:
    print('Parabéns, você acertou! O número escolhido foi o {}'.format(numPC))
else:
    print('Que pena! O núemro escolhido foi o {}, você digitou {}'.format(numPC, numUser))
