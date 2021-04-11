# Condições #

nome = input('Qual o seu nome?')
# Condição simples
if nome == 'Carolina':
    print('Que nome lindo você tem!')
print('Bom dia, {}!'.format(nome))


tempo = int(input('Quantos anos tem seu carro?'))
# Condição simplificada
print('Carro novo' if tempo <= 3 else 'Carro velho')

# Condição complexa
if tempo <= 3:
    print('Seu carro está novinho!')
else:
    print('Vixe, seu carro está um pouco velho...')


