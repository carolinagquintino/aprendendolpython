# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

cidade = input('Insira o nome da cidade: ')
prim = cidade.split()

print('SANTO' in prim[0].upper())
