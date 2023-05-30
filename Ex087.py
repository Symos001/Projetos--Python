# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
s = mai=colun = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o numero na posição[{l}][{c}]:'))
print('A matriz completa é :')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
        if matriz[l][c] % 2 == 0:
            s += matriz[l][c]
        if l == 1:
            if matriz[l][c] > mai:
                mai = matriz[l][c]
        if c == 2:
            colun += matriz[l][c]
    print()

print(f'A soma de todos os numeors pares é: {s}')
print(f'A soma dos valores da terceira coluna é: {colun}')
print(f'O maior valor da segunda linha é : {mai}')

