# Crie um programa que declare uma matriz de dimensão 3×3
# e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for L in range(0, 3):
    for c in range(0, 3):
        matriz[L][c] = int(input(f'Digite um numero na posição[{L},{c}] :'))
print('-='*30)
for L in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[L][c]}]', end='')
    print()