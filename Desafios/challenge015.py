# Escreva um programa que pergunta a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos ...
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado

kmCorr = float(input(('Quantos Km foram percorridos? ')))
dias = int(input('Foi alugado por quantos dias? '))

valKm = kmCorr * 0.15
valDias = dias * 60

total = valKm + valDias

print('O preço a pagar é R${} dos Km percorridos + R${} dos dias alugados, que totaliza R${}.'
      .format(valKm, valDias, total))
