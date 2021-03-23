# Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Insira o salário atual: '))
novo = salario * 1.15
print('Parabéns, você teve um aumento de 15% no seu salário!! \n De R${} você passou a ganhar R${:.2f}'.format(salario, novo))
