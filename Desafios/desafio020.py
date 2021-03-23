# O mesmo professor do desafio anterior quer sortear a ordem de apresetação de trabalhos dos alunos. Faça um programa ...
# que leia o nome dos quatro alunos e mostre a ordem sorteada

import random

a1 = input('Insira o nome de um aluno(a): ')
a2 = input('Insira o nome de um aluno(a): ')
a3 = input('Insira o nome de um aluno(a): ')
a4 = input('Insira o nome de um aluno(a): ')

lista = [a1, a2, a3, a4]

print('A ordem de apredentação dos alunos será: {}'.format(random.sample(lista, k=4)))
# random.shuffle(lista)
