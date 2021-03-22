# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input('Insira o valor atual do produto: '))
novo = preco * 0.95
print('OFERTA!! De R${} por apenas R${}!!!'.format(preco, novo))
