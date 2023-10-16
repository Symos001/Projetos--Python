#Exercício Python 078: Faça um programa que leia
# 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado
# e as suas respectivas posições na lista.

numeros =[] #lista de numeros (lista 1)
numerosdes=[] #lista dos numeros desorgarganizados (lista 2)

for c in range(0,5): #a estrutura de repetição dar espaço
                     #ao usuario adicionar valores e vai coloca-los em duas listas
    n = int(input('Digite um numero :'))
    numeros.append(n) #a primeira é a lista que será organizada
    numerosdes.append(n) #a segunda é a lista que permanescerá desorganizada

numeros.sort() #coloca a lista 1 em ordem numérica

#dai para encontrar o maior ou o menor valor é só colocar a posição deles na lista
print(f'O Maior valor digitado foi {numeros[4]},nas posições',end='')

for i,v in enumerate(numerosdes): #esta estrutura "for" indexa os valores da lista 2
                                  # e se o valor for igual ao maior numero ele irá mostrar a posição des numero
    if v == numeros[4]:
        print(f' {i+1}...',end='')
print()
print(f'O Menor valor digitado foi {numeros[0]},nas posições ',end='')
for i,v in enumerate(numerosdes):#esta estrutura "for" indexa os valores da lista 2
                                 # e se o valor for igual ao menor numero ele irá mostrar a posição des numero
    if v == numeros[0]:
        print(f'{i+1}...',end='')