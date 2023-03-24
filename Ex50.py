#Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for c in range(1,7):
    n1 = float(input('Digite o {}º valor :'.format(c)))
    if n1 % 2 == 0 :
        soma += n1
        cont += 1
if soma ==0 or cont ==0:
    print('Você informou apenas numeros IMPARES')
else :
    print('desses {} valores PARES , se forem somados, teremos {}'.format(cont,soma))

