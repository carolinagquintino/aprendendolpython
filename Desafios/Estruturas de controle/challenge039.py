'''
Faça um programa que leia o ano de nascimento de um jovem e imforme, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
'''

from datetime import date

sexo = input('Qual seu sexo? ')

if sexo[0].lower().strip() == 'f':
    print('Bom dia!')
elif sexo[1].lower().strip() != 'u' and sexo[0].lower().strip() == 'm':
    ano = int(input('Em qual ano você nasceu? '))
    idade = date.today().year - ano

    if idade == 18:
        mes = int(input('E em qual mês? '))
        if date.today().month < mes:
            print('Daqui {} meses você terá que se alistar ao Serviço Militar'
                  .format(mes - date.today().month))
        else:
            print('Você está na idade certa para realizar o alistamento ao Serviço Militar,'
                  'deve se alistar até {}/{}'.format(mes, ano + 19))
    elif idade == 19:
        mes = int(input('E em qual mês? '))
        if date.today().month < mes:
            print('Você está na idade certa para realizar o alistamento ao Serviço Militar, '
                  'deve se alistar até o mês {}'.format(mes))
        else:
            print('Você passou {} meses do prazo, deveria ter se alistado ate o mês {}'
                  .format(date.today().month - mes, mes))
    elif idade < 18:
        print('Você está com {} anos. Daqui {} anos você terá que se alistar ao Serviço Militar, em {}'
              .format(idade, 18 - idade, ano + 18))
    elif idade > 18:
        print('Você tem {} anos, já passou {} anos do prazo. Deveria ter se alistado em {}/{}'
              .format(idade, idade - 18, ano + 18, ano + 19))
