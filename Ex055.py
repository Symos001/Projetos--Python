# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
cont = 0
cont2 = 0
for p in range(1, 6):
    peso = float(input('Digite o peso da {}º pessoa :'.format(p)))

    if p == 1:
        maior = peso
        menor = peso

    else:
        if peso > maior:
            cont = p
            maior = peso

        elif peso < menor:
            cont2 = p
            menor = peso

print('O maior peso é da {}º pessoa , tendo {} kg'.format(cont, maior))
print('O menor peso é da {}º pessoa , tendo {} kg'.format(cont2, menor))
