#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso

import time
print('Bem vindo ao programa de operações!!')
time.sleep(1)

n1=int(input('Digite o primeiro numero: '))
n2=int(input('Digite o segundo numero: '))
op=0

time.sleep(1)
while op != 5 :
    print('=-' * 20)
    print('''isso é o que eu posso fazer !!
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa''')
    print(' ')
    print('=-'*20)

    op= int(input('>>>que operação gostaria de fazer ? '))

    if op == 1:
        soma = n1 + n2
        print('a soma entre {} e {} é {}'.format(n1,n2, soma))

    elif op == 2:
        mult = n1 * n2
        print('a multiplicação de {} e {} é {}'.format(n1,n2,mult))
    elif op == 3:
        if n1 > n2:
            print('entre {} e {},o maior é {}'.format(n1,n2,n1))
        elif n1 < n2:
            print('Entre {} e {},o maior é {}'.format(n1,n2,n2))
        elif n1 == n2:
            print("Os dois são iguais, portanto não há maior")
    elif op == 4:
        n1 = int(input('Digite o primeiro numero : '))
        n2 = int(input('Digite o segundo numero :'))
print('Até a proxima!!')