# Faça um programa que leia o comprimento de cateto oposto e do cateto adjacente de um triângulo retângulo, calcule ...
# e mostre o comprimento da hipotenusa

from math import hypot

c1 = float(input('Insira o primeiro cateto: '))
c2 = float(input('Insira o segundo cateto: '))
hip = hypot(c1, c2)

print('A hipotenusa de um triângulo cujo os catetos medem {} e {} é {:.2f}.'.format(c1, c2, hip))
