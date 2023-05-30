#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado
# e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
jogadores={}

for c in range(1,5):
    jogadores[f'Jogador {c}'] = randint(1,6)
print('Valores sorteados:')
for k,v in jogadores.items():
    print(f'O {k} ,tirou: {v} ')
    sleep(1)
print('-='*30)
print(' '*8,end='')
print('==RANQUING DE JOGADORES:==')
c=0
print(' '*5,end='')
print('_'*33)
for i in sorted(jogadores, key =jogadores.get, reverse=True):
    c+=1
    print(f'     {c}º lugar está {i}, com: {jogadores[i]}.')
    sleep(1)





