# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50
# por Km para viagens de até 200Km e R$0,45 para viagens mais longas

dist = float(input('Qual a distância em Km da sua viagem? '))
print('Você fará uma vaigem de {}Km'.format(dist))

preco = dist * 0.5 if dist <= 200 else dist * 0.45

''' if dist <= 200:
    preco = dist * 0.5
else:
    preco = dist * 0.45 '''

print('Sua passagem custará R${:.2f}'.format(preco))

