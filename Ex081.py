# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
num5 = []
cont = 0
r = ""
while True: # a estrutura while adiciona valores
            # e se o numero 5 for adicionado ele irá contar
    n = int(input("Digite um numero :"))
    lista.append(n)
    if n == 5:
        cont += 1
    while True:
        r = str(input("Quer continuar ? [S/N]"))[0].strip()
        if r in "SsNn":
            break
    if r in "Nn":
        break

lista.sort(reverse=True) #esse comando coloca a lista em ordem decrescente
for i, v in enumerate(lista): # essa estrutura utiliza o enumerate
                              # para encontrar a posição do 5 se estiver na "lista"
                              # ele joga a posição dele para a lista : num5
    if v == 5:
        num5.append(i+1)

print(f"Foram digitados {len(lista)} numeros ")
print(f"Sendo em ordem decrescente {lista}")
if 5 in lista: #se o valor 5 estiver na lista ele irá mostrar quantos tem , e qual é a sua respectiva posição
    print(f"O numero 5 esta na lista ,sendo que a lista contem {cont}")
    print(f'Estando nas posições {num5}, em ordem decrescente')
else:
    print('O numero 5 não esta na lista ')
