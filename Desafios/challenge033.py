# Faça um programa que leia três números e mostre qual é o maior e qual é o menor

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Último número a ser digitado: '))

if n1 > n2 and n1 > n3:
    print('O primeiro número, {}, é o maior entre {}, {} e {}'.format(n1, n1, n2, n3))
elif n2 > n1 and n2 > n3:
    print('O segundo número, {}, é o maior entre {}, {} e {}'.format(n2, n1, n2, n3))
elif n3 > n1 and n3 > n2:
    print('O terceiro número, {}, é o maior entre {}, {} e {}'.format(n3, n1, n2, n3))
