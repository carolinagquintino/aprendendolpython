'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''

print(f'{" Loja da Carol ":=^40}')

valor = float(input('Valor da compra? R$'))
print('''FORMAS DE PAGAMENTO
      [1] Dinheiro
      [2] Cheque
      [3] Cartão''')
pag = int(input('Qual a opção de pagamento? '))

if pag == 1 or pag == 2:
    desconto = valor * 0.9
    print('Você terá um desconto de 10% na sua compra de R${:.2f}\n'
          'O novo total da sua compra é de R${:.2f}'.format(valor, desconto))
elif pag == 3:
    parcelas = int(input('Quantas parcelas deseja? '))

    if parcelas == 1:
        desconto = valor * 0.95
        print('Você terá um desconto de 5% na sua compra de R${:.2f}\n'
              'O novo total da sua compra é de R${:.2f}'.format(valor, desconto))
    elif parcelas == 2:
        print('O total da sua compra é de R${:.2f}\n'
              'Serão 2 parcelas de R${:.2f} cada'.format(valor, valor / 2))
    else:
        juros = valor * 1.2
        print('Essa forma de pagamento adicionará 20% de juros no seu pedido de R${:.2f}\n'
              'O novo total da sua compra é de R${:.2f}\n'
              'Serão {} parcelas de R${:.2f} cada'.format(valor, juros, parcelas, juros / parcelas))
else:
    print('Opção de pagamento inválida!')
