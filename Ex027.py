#Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome= str(input('Digite seu nome completo :' )).strip()
prim= nome.split()
print('O seu primeiro nome é {}'.format(prim[0]))
print('O seu ultimo nome é {}'.format(prim[len(prim)-1]))
