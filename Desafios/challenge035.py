# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
# triângulo

l1 = float(input('Digite o comprimento de uma reta: '))
l2 = float(input('Digite o comprimento da segunda reta: '))
l3 = float(input('Digite o comprimento da última reta: '))

if l1 > l2 and l1 > l3:
    if l2 + l3 <= l1:
        print('Vixe, essas retas não formam um triângulo.')
    else:
        print('Eba! Essas retas formam um triângulo')
elif l2 > l1 and l2 > l3:
    if l1 + l3 <= l2:
        print('Vixe, essas retas não formam um triângulo.')
    else:
        print('Eba! Essas retas formam um triângulo')
elif l3 > l1 and l3 > l2:
    if l1 + l2 <= l3:
        print('Vixe, essas retas não formam um triângulo.')
    else:
        print('Eba! Essas retas formam um triângulo')
