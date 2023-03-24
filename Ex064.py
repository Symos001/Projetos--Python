#Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados
# e qual foi a soma entre eles (desconsiderando o flag)
print("-"*10)
print("SOMANDO")
print("-"*10)
n = cont = soma = 0
while n != 999:
    n = float(input("Digite um numero [999 para parar]:"))
    if n != 999:
        cont += 1
        soma += n
print("A quantidade de numeros digitados foi de {},e a soma deles é {}".format(cont,soma))