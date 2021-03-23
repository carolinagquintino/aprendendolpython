# Manipulando texto #

frase = 'Curso em Vídeo Python'
fraseE = '   Aprenda Pytohn  '
print(frase)
print(fraseE)

print('-' * 12)

# Fatuamento
print(frase[9])
print(frase[9:14])  # o último valor não entra na contagem
print(frase[9:21:2])  # saltar de 2 em 2
print(frase[:5])  # a partir do inicio
print(frase[15:])  # até o fim
print(frase[9::3])  # até o fim e de 3 em 3

print('-' * 12)

# Análise
print(len(frase))  # comprimento
print(frase.count('o'))  # conta quantas vezes
print(frase.count('o', 0, 13))  # conta quantas vezes e fatia
print(frase.find('deo'))  # mostra em que posição começou
print(frase.find('Andoid'))  # se não existir retorna -1
print('Curso' in frase)  # existe ou não

print('-' * 12)

# Transformação
print(frase.replace('Python', 'Android'))  # substitui
print(frase.upper())  # capitaliza todas as letras
print(frase.lower())  # descaptaliza todas as letras
print(frase.capitalize())  # deixa apenas a primeira letra maiúscula
print(frase.title())  # capitaliza a primeira letra de cada palavra
print(fraseE.strip())  # remove os espaços desnecessários
print(fraseE.rstrip())  # remove os espaços da direita
print(fraseE.lstrip())  # remove os espaços da esquerda

print('-' * 12)

# Divisão
print(frase.split())  # dividir a string pelos espaços e cria uma lista

print('-' * 12)

# Junção
print('-'.join(frase))  # junta e adiciona

print('-' * 12)

# Texto longo
print("""Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.""")  # 3 aspas duplas
