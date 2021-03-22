# Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada

num = int(input('Digite um número: '))
dob = num * 2
tri = num * 3
raiz = num ** (1/2)
print('O dobro do número {} é {}, o triplo é {} e a raiz quadrada é {}'.format(num, dob, tri, raiz))
