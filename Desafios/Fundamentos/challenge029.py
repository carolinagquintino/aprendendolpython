# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensafem dizendo que
# ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Em que velocidade o carro está? '))

if velocidade > 80:
    # acima = velocidade - 80
    # multa = acima * 7
    multa = (velocidade - 80) * 7
    print('Sua velocidade está acima do limite permitido de 80Km/h. Você terá uma multa de R${:.2f}'.format(multa))

print('Pode prosseguir, tenha um bom dia!')