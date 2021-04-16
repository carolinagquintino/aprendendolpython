'''
Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
'''

peso = float(input('Qual o seu peso em quilos? '))
altura = float(input('Qual a sua altura em metros? '))
imc = peso / (altura ** 2)

print('O seu IMC é de {:.1f}, isso significa que você está '.format(imc), end='')
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('no Peso ideal')
elif imc < 30:
    print('com Sobrepeso')
elif imc < 40:
    print('com Obesidade')
else:
    print('com Obesidade mórbida')
