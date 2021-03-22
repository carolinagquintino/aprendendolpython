# Escreva um programa que converta uma temperatura digitada em °C e converta para °F

tempC = float(input('Insira a temperatura em °C: '))
tempF = tempC * 1.8 + 32
print('A temperatura {}°C em °F é {}.'.format(tempC, tempF))
