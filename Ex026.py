# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
ltr = str(input('Digite uma frase :')).strip()
frase = ltr.upper()
contar = frase.count('A')

print('A quantidade de vezes que aparece a letra, A , é {}'.format(contar))
print('A posição que a letra A aparece na primeira vez é {},'.format(frase.find('A')+1))
print(' A posição que a letra aparece na ultima vez é {} '.format(frase.rfind('A')+1))

