#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import *
from time import *
lista = [[]]
j = int(input('quantos jogos vão ser criados ?'))
n=0
for c in range (0,j):
    if j >= c:
        lista.append([] * j)
    for l in range (0,6):
        n= randint(1,60)
        lista[c].append(n)
print(f'Aqui esta sorteando {j} jogos :')
for c in range(0,j):
    sleep(1)
    lista[c].sort()
    print(f'JOGO {c+1}: {lista[c]}')