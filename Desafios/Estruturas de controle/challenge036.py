'''
Escreva um programa para aprovar o empréstimo bancário para aprovar a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele
vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''

print('=-=' * 13)
print('Bem vindo(a) ao Simulador de Empréstimo')
print('=-=' * 13)

valor = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = int(input('Em quantos anos irá pagar? '))

prestacao = valor / (anos * 12)

print('O valor das prestações mensais de uma casa de R$ {:.0f} mil, que irá ser paga em {} anos, é de R$ {:.2f}.'.format(valor // 1000, anos, prestacao))

if prestacao > salario * 0.3:
    print('Esse valor condiz com {:.0f}% do seu salário, infelizmente não podemos aprovar o seu empréstimo.'.format(prestacao * 100 / salario))
else:
    print('Esse valor condiz com {:.0f}% do seu salário. Seu empréstimo pode ser aprovado!'.format(prestacao * 100 / salario))
