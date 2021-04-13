# Faça um programa que leio o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
    # Ex: Ana Maria de Souza
    # primeiro = Ana
    # último = Souza

nome = input('Insira seu nome: ').strip()

print('Primeiro nome: {}'.format(nome[:nome.find(' ')]))
print('Último nome: {}'.format(nome[nome.rfind(' '):]))

# n = nome.split()
# print('Primeiro nome: {}'.format(n[0]))
# print('Último nome: {}'.format(n[len(n) - 1]))
