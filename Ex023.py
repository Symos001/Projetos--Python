# Faça um programa que leia um número de 0 a 9999
# e mostre na tela cada um dos dígitos separados.
n= int(input('Digite um Numero'))
u= n // 1 % 10
d= n // 10 % 10
c= n // 100 % 10
M= n // 1000 % 10
print('a Unidade é : {}'.format(u))
print('a Dezena é : {}'.format(d))
print('a Centena é : {}'.format(c))
print('o Milhar é : {}'.format(M))


