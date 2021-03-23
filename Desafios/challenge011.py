# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a ...
# quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m²

altura = float(input('Insira a altura da parede em metros: '))
largura = float(input('Insira a largura da parede em metros: '))
area = altura * largura
tinta = area / 2
print('Para cobrir a parede de {}m de área inteira precisará de {} litros de tinta'.format(area, tinta))
