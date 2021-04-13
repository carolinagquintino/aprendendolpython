'''
Cores no terminal

Padrão ANSI
\033[   m

1 style  2 text  3 back

Style:
0 none
1 bold
4 underline
7 negative

Text:
30 preto
31 vermelho
32 verde
33 amarelo
34 azul
35 roxo
36 ciano
37 cinza

Back:
40 preto
41 vermelho
42 verde
43 amarelo
44 azul
45 roxo
46 ciano
47 cinza

Exemplo: \033[ 0;33;44 m
'''

print('\033[0:0:41m Teste \33[m')
print('\033[4:33:44m Teste \33[m')
print('\033[1:35:43m Teste \33[m')
print('\033[0:42m Teste \33[m')
print('\033[0:40m Teste \33[m')
print('\033[7:0:40m Teste \33[m')
