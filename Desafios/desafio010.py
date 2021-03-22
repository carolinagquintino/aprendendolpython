# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# US$ 1,00 = R$ 3,27

reais = float(input('Quanto dinheiro você tem na carteira? '))
dolar = 5.49
conver = reais / dolar
print('Com R${:.2f} reais você pode comprar US${:.2f} dálares.'.format(reais, conver))