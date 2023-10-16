# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares
# e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

val = []
par = []
impar = []
r = ''
while True:
    n = int(input("Digite um valor:"))
    val.append(n)
    if n % 2 == 0:
        par.append(n)
    elif n % 2 == 1:
        impar.append(n)
    while True:
        r = str(input('Quer continuar [S/N] ?'))[0]
        if r in 'SsNn':
            break
    if r in 'Nn':
        break
print(f'Os valores da lista são :{val}')
print(f"Os valores da lista que são pares são {par}")
print(f'Os valores da lista que são impares são {impar}')
