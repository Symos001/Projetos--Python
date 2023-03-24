# Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

contma = contme = maior = menor = soma = quant = media = 0
continuar = "s"
while continuar in "s":
    n = float(input("Digite seu número : "))
    quant += 1
    soma += n
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            contma = quant
            maior = n
        elif n < menor:
            contme = quant
            menor = n
    continuar = str(input("Quer continuar? [S/N] ")).strip().lower()[0]
media = soma / quant
if contma == 0:
    contma += 1
elif contme == 0:
    contme += 1
print("A média desses {} valores é {:.2f}, ".format(quant, media))
print("Sendo que o maior é o {}º numero de valor {} ".format(contma, maior))
print("E o menor é o {}º numéro de valor {} ".format(contme, menor))
