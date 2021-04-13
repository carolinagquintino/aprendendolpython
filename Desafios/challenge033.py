# Faça um programa que leia três números e mostre qual é o maior e qual é o menor

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Último número a ser digitado: '))

# Verifica maior
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3

# Verifica menor
if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3

print('O maior número é o {} e o menor é o {}'.format(maior, menor))
