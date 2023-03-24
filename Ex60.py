#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#5! = 5 x 4 x 3 x 2 x 1 = 120
import time
print("Calculador de fatoriais!!")
time.sleep(1)
fatorial = 0
cont = 0
n2 = 0
n1 = int(input('Digite seu numero: '))
cont2 = n1

while n2 != 1 :
    cont += 1
    n2 = (n1 -cont)
    if fatorial == 0:
        fatorial = (n1) * (n2)
    else:
        fatorial = (fatorial) * (n2)

print('{}!='.format(n1), end='')

while cont2 > 0:
    print('{}'.format(cont2),end='')
    print(' x ' if cont2 >1 else '=',end='')
    cont2 -= 1

print('{}'.format(fatorial))
