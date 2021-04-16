'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade
- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Junior
- Até 25 anos: Sênior
- Acima: Master
'''

from datetime import date

ano = int(input('Qual seu ano de nascimento? '))
mes = int(input('E qual o mês de nascimento? '))
idade = date.today().year - ano

if date.today().month < mes:
    idade = idade - 1

if idade <= 9:
    print('O atleta tem: {} anos\nA sua categoria é: Mirim'.format(idade))
elif idade <= 14:
    print('O atleta tem: {} anos\nA sua categoria é: Infantil'.format(idade))
elif idade <= 19:
    print('O atleta tem: {} anos\nA sua categoria é: Junior'.format(idade))
elif idade <= 25:
    print('O atleta tem: {} anos\nA sua categoria é: Sênior'.format(idade))
else:
    print('O atleta tem: {} anos\nA sua categoria é: Master'.format(idade))

#CATEGORIAS
'''
mirim = range(0, 10)
infatil = range(10, 15)
junior = range(15, 20)
senior = 20
'''

#CONDIÇÕES
'''
if idade in mirim:
    print('MIRIM. O aluno tem {} anos, então se encaixa nessa categoria.'.format(idade))
elif idade in infatil:
    print('INFANTIL. O aluno tem {} anos, então se encaixa nessa categoria.'.format(idade))
elif idade in junior:
    print('JUNIOR. O aluno tem {} anos, então se encaixa nessa categoria.'.format(idade))
elif idade == senior:
    print('SENIOR. O aluno tem {} anos, então se encaixa nessa categoria.'.format(idade))
else:
    print('MASTER. O aluno tem {} anos, então se encaixa nessa categoria.'.format(idade))
'''
