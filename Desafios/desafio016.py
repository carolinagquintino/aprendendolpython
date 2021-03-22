# Crie um programa que leia um número pelo teclado e mostre na tela a sua porção inteira
# Ex: Digite um número: 6.127. O número 6.127 tem a parte inteira 6.

from math import trunc
n = float(input('Insira um número decimal: '))
print('A parte inteira de {} é {}'.format(n, trunc(n)))
