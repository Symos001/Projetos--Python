#Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
from time import sleep
n1 = int(input('Digite um numero inteiro :'))

print('Em qual base gostaria de converter ?')
sleep(1)
print('[ 1 ] para binário')
sleep(1)
print('[ 2 ] para octal')
sleep(1)
print('[ 3 ] para hexadecimal')
sleep(1)
op = int(input('Sua opção :'))

if op == 1:
    print('Seu numero {} convertido para binário é {}'.format(n1,bin(n1)[2:]))
elif op == 2:
    print('Seu numero {} convertido para octal é {}'.format(n1,oct(n1)[2:]))
elif op == 3:
    print('Seu numero {} convertido para hexadecimal é {}'.format(n1,hex(n1)[2:]))
else:
    print('Opção inválida, tente novamente')