#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando
# o recurso de mostrar que tipo de triângulo será formado:

# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes
from time import sleep
print('\33[34m+-=\33[m'*20)
print('\33[34mANALIZADOR DE TRIANGULOS V2\33[m')
print('\33[34m+-=\33[m'*20)

a = float(input('Digite o comprimento de A :'))
b = float(input('Digite o comprimento de B :'))
c = float(input('Digite o comprimento de C :'))

print('\33[34m+-=\33[m'*20)
print('\33[34mANALIZANDO...\33[m')
print('\33[34m+-=\33[m'*20)
sleep(2)
if a + b > c and a + c > b and b + c > a: #Verifica se é possivel cirar um triangulo a partir desses segumentos
    print('Esses seguimentos {} PODEM FORMAR {} um triangulo!'.format('\33[32m','\33[m'), end='')
    if a==b==c:#Verifica se é um triangulo equilatero
        print( '\33[32mEQUILÁTERO[m!!!\33[m')
        print('Pois todos os lados são iguais !!!')

    elif a==b or b==c or a==c:#verifica se é um triangulo isóceles
        print('\33[32mISÓCELES!!!\33[m')
        print('Pois dois lados são iguais')

    elif a != b and a != c and b != c:#verifica se é um triangulo escaleno
        print('\33[32mESCALENO!!!\33[m')
        print('Pois todos os lados são diferentes')
else:
    print('\33[31mEsses seguimentos NÃO PODEM FORMAR um triangulo\33[m')