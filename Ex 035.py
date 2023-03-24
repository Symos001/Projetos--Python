#Desenvolva um programa que leia o comprimento de três retas
# e diga (ao usuário se elas podem ou não formar um triângulo.

print('-='*20)
print('Analisador de triangulos')
print('-='*20)
a = float(input('Digite a comprimento do primeiro seguimento:'))
b = float(input('Digite o comprimento do segundo seguiemento:'))
c = float(input('Digite o comprimento do terceiro seguimento:'))

if a + b > c and a + c > b and b + c > a:
    print('Esses seguimentos podem formar um triangulo!')

else:
    print('Esses seguimentos não formam triangulos ')