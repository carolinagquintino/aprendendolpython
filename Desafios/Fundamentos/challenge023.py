# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
    # ex: Digite um número: 1834
        # unidade: 4
        # dezena: 3
        # centena: 8
        # milhar: 1

num = input('Digite um número entre 0 e 9999: ')
print('Unidade: ', num[3])
print('Dezena: ', num[2])
print('Centena: ', num[1])
print('Milhar: ', num[0])

# n = int(input('Informe um número entre 0 e 9999: '))
# u = n // 1 % 10
# d = n // 10 % 10
# c = n // 100 % 10
# m = n // 1000 % 10
#
# print('Unidade: ', u)
# print('Dezena: ', d)
# print('Centena: ', c)
# print('Milhar: ', m)
