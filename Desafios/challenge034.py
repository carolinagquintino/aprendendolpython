# Escreva um programa que pergunte o salário de um funcionário e calcula o valor do seu aumento. Para salários
# superiores a R$1.250.00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Qual o seu salário? R$ '))

if salario <= 1250:
    aumento = salario * 1.1
else:
    aumento = salario * 1.15

print('Parabéns, você recebeu um aumento! Seu novo salário será de R${:.2f}'.format(aumento))
