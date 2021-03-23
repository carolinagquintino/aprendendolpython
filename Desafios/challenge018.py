# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

ang = float(input('Insira um ângulo: '))
seno = math.sin(math.radians(ang))
coss = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

print('O seno do ângulo {} é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(ang, seno, coss, tang))
