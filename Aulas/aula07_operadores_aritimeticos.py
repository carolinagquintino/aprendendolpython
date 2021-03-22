# Operadores aritméticos #
# + adição
# - subtração
# * multiplicação
# / divisão
# ** potência
# // divisão inteira
# % resto da divisão
# == igual

# Ordem de precedência #
# ()
# **
# * ; / ; // ; %
# + ; -

# raiz quadrada **(1/2)
# raiz cubica **(1/3)

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
e = n1 ** n2
print('A divisão inteira é {}, o resto {}, a potência {}'.format(di, r, e), end=' ')  # end='': insere no final da linha
print('A soma é {}, o produto {}, a divisão {:.3f}'.format(s, m, d))  # formatação com 3 casas decimais flutuantes


nome = input('Informe seu nome: ')
print('Prazer em te conehcer {:>20}!'.format(nome))  # formata a direita em 20 casas decimais
print('Prazer em te conehcer {:=^20}!'.format(nome))  # formata centralizado com = em volta

