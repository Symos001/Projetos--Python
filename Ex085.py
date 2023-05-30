# Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

numeros = [[], []]
n=0
for c in range(0, 7):
    n = int(input('Digite um numero:'))

    if n % 2 == 0:
        numeros[0].append(n)

    else:
        numeros[1].append(n)

numeros[0].sort()
numeros[1].sort()
print(f'Dos numeros que você digitou ')
print(f'os numeros impares são :{numeros[1]}')
print(f'os numeros pares são : {numeros[0]}')
