# Crie um programa que leio o nome completo de uma pessoa e mostre:
    # O nome com todas as letras maiúsculas
    # O nome com todas minúsculas
    # Quantas letras ao to.do (sem considerar os espaços)
    # Quantas letras tem o primeiro nome

nome = input('Insira seu nome: ').strip()
div = nome.split()

print('Maiúsculo: ', nome.upper())
print('Minúsculo: ', nome.lower())
print('Quantidade letras ao todo: ', len(nome) - nome.count(' '))
# print('Quantidade letras primeiro nome: ', len(div[0]))
print('Quantidade letras primeiro nome: ', nome.find(' '))
