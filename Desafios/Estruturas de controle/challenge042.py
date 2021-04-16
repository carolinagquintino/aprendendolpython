'''
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
'''

r1 = int(input('Insira a medida de uma reta: '))
r2 = int(input('Insira a medida de outra reta: '))
r3 = int(input('Insira a medida da última reta: '))

if r1 + r2 < r3 and r2 + r3 < r1 and r3 + r1 < r2:
    print('SInto informar, mas essas retas não formam um triângulo.')
elif r1 == r2 == r3:
    print('Todos os lados desse triângulo medem {}, ele é um triângulo equilátero.'.format(r1))
elif r1 == r2 or r2 == r3 or r1 == r3:
    print('Esse triângulo tem 2 lados iguais, ele é um triângulo isóceles')
else:
    print('Todos os lados desse triângulo são diferentes, ele é um triângulo escaleno')