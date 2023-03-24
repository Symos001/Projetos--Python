# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
frase = str(input('Digite uma frase : ')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inverso = ''
for letra in range(len(juntar)-1,-1 ,-1):
   inverso += juntar[letra]
print('A sua frase é {}, invertida ela fica {}'.format(juntar,inverso))

if inverso == juntar:
    print('Ela é um palindromo!!')
else :
    print('Ela não é palindromo')

