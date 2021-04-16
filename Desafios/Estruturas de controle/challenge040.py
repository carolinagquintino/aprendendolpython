'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''

nota1 = float(input('Qual foi a nota obtida na primeira avaliação? '))
nota2 = float(input('Qual foi a nota obtida na segunda avaliação? '))

media = (nota1 + nota2) / 2

print('Sua média foi de {:.1f}'.format(media))

if media < 5:
    print('Sinto muito, mas essa pontuação não é suficiente para aprovação!')
elif media < 6.9:
    print('Sinto muito, mas essa pontuação indica recuperação!')
else:
    print('Parabéns! Você foi aprovado.')
