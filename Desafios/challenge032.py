# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

from datetime import date

ano = input('Digite um ano ou "atual" para o ano atual: ')

if ano == 'atual':
    ano = date.today().year  # verifica o ano atual da máquina

if int(ano) % 4 == 0 and int(ano) % 100 != 0 or int(ano) % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))

'''
if str(ano)[2:].strip() == '00':
    if ano % 400 == 0:
        print('O ano {} é bissexto'.format(ano))
    else:
        print('O ano {} não é bissexto'.format(ano))
elif ano % 4 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
'''