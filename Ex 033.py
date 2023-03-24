#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = float(input('Digite um número :'))
n2 = float(input('Digite um número :'))
n3 = float(input('Digite um número :'))

# Verificando quem é o maior
maior = n1

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
print('o maior numero é {}'.format(maior))

# Verificando quem é o menor
menor = n1

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print( 'o menor número é {}'.format(menor))
