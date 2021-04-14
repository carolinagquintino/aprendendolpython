'''
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''

prim = int(input('Digite um valor: '))
segun = int(input('Digite mais um valor: '))

if prim == segun:
    print('Opa! Os dois valores são iguais')
elif prim > segun:
    print('O primeiro valor é o maior')
else:
    print('O segundo valor é o maior')
