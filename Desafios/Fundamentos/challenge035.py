# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
# triângulo

l1 = float(input('Digite o comprimento de uma reta: '))
l2 = float(input('Digite o comprimento da segunda reta: '))
l3 = float(input('Digite o comprimento da última reta: '))

if l1 < l2 + l3 and l2 < l3 + l1 and l3 < l1 + l2:
    print('Eba! Essas retas formam um triângulo')
else:
    print('Vixe, essas retas não formam um triângulo.')
