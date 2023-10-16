# Faça um programa que tenha uma lista chamada
# números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los
# dentro da lista e a segunda função vai mostrar a soma
# entre todos os valores pares sorteados pela função anterior.

from random import *
from time import sleep
def sorteia(n):
    for c in range(0, 5):
        print("=", end='')
        sleep(0.5)
    print(">SORTEANDO NUMEROS")
    print(f">>Sorteado ", end="")
    for c in range(0,5):
        num= randint(0,10)
        n.append(num)
        print(f"{num}",end=' ')
        sleep(0.3)




def somaPar(num):
    par = 0
    impar = 0
    for i,v in enumerate(num):
        if v % 2 == 0:
            par+=v
        else:
            impar+=v
    print(f"A soma de todos os valores pares é {par}")
    print(f"A soma de todos os valores impares é {impar}")

# programa principal
numeros = []
foradalista=[]
print("SOTEADOR E SOMADOR DE NUMEROS!!")

sorteia(numeros)
print(' ')
somaPar(numeros)