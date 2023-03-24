#Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Exemplo:
#0 – 1 – 1 – 2 – 3 – 5 – 8
#F(n + 2) = F(n + 1) + F(n) , com n ≥ 1 e F(1) = F(2) = 1
print("-"*40)
print("SEQUENCIA DE FIBONACCI")
print("-"*40)
n1= int(input("Quantos termos você quer mostrar ? "))
cont = 3
t1 = 0 #primeiro termo
t2 = 1 #segundo termo

print("{}-> {}->".format(t1,t2), end=" ")
while cont <= n1:
    t3 = t1 + t2 #o terceiro termo é a soma deles
    print("{}->".format(t3),end=' ')
    #aqui os termos são realocados dessa maneira o primeiro termo
    #dessa maneira o primeiro e o segundo termo se tornam os posteriores da sequencia
    #Como RnaM
    t1 = t2
    t2 = t3
    cont += 1
print("Fim")