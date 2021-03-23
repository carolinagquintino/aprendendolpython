# Faça um programa que leia uma frase pelo teclado e mostre:
    # Quantas vezes aparece a letra "A"
    # Em que posição ela aoarece pela primeira vez
    # Em que posição ela aparece pela última vez

frase = input('Digite livremente: ').strip()
print('Na frase: {}, notamos '.format(frase))
print('{} vezes a letra "A"'.format(frase.upper().count('A')))
print('A letra "A" aparece pela primeira vez na {}° posição'.format(frase.upper().find('A') + 1))
print('A letra "A" aparece pela última vez na {}° posição'.format(frase.upper().rfind('A') + 1))
