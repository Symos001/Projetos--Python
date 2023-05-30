#Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento)
# e mostre a área do terreno.

def area(lar,comp):
    ar=lar*comp
    print(f'A area com {l} de largura por {c} de comprimento, é igual a {ar}m')


#Programa principal
l= float(input('Digite o tamanho da largura(m):'))
c= float(input('Digite o tamanho do comprimento(m):'))
print('--'*30)
area(l,c)