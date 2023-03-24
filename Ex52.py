# Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.
n = int(input('Digite para descobrir se ele é primo :'))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\33[32m', end=' ')
        tot += 1
    else:
        print('\33[m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\33[mO numero {}, foi divisivel {} vezes '.format(n, tot))

if tot == 2:
    print('Esse numero é primo!!')
else:
    print('Esse numero não é primo!!')

