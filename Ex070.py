#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.

# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

print("{:-^40}".format("SUPER MERCADO BOM PREÇO"))
tot = soma = mil = menor = 0
barato = ''
while True:
    nome = str(input('Produto:')).upper().strip()
    preco = float(input('Preço : R$'))
    tot+=1
    soma+=preco
    if preco > 1000:
        mil += 1
    if tot == 1 or preco < menor :
        menor = preco
        barato = nome
    resp = ' '
    while resp not in 'SN':
        resp= str(input('quer continuar ? ')).upper().strip()[0]
    if resp == 'N':
        break
print("{:-^40}".format("FIM DO PROGRAMA"))
print(f"O total gasto na compra foi de {soma:.2f}")
print(f"A quantidade de produtos que custam mais de R$1000,00 é de {mil}")
print(f"O produto mais barato é o {barato}, no valor de R${menor:.2f}")
