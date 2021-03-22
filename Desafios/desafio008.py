# Escreva um programa que leia um valor em metros e o exiba convertido em centimentros e milímetros

m = float(input('Insira um valor em metros: '))
cm = m * 100
mm = m * 1000
print('{} metros \n {:.0f} centímetros \n {:.0f} milímetros'.format(m, cm, mm))
