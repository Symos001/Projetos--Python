# Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

import time


def contador(i, f, p):
    print('-=' * 30)
    print(f'Contagem de {i} até {f} de {p * -1 if p < 0 else p * 1} em {p * -1 if p < 0 else p * 1}:')
    time.sleep(2.5)
    for c in range(i, f + 1 if f > 0 else f - 1, p):
        print(c, end=' ')
        time.sleep(0.5)
    print('FIM!!')


# Programa principal
contador(1, 10, 1)
contador(10, 0, -2)
print('Agora é a sua vez de personalizar a contagem:')
ini = int(input('Inicio:'))
fim = int(input('Fim:'))
pas = int(input('Passo:'))
contador(ini, fim, pas)
