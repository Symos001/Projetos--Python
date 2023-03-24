# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
#import emoji':right_arrow:'

primterm = int(input('Qual é o primeiro termo da PA ?'))
razao = int(input('Qual é sua razão ?'))
Quantidade = int(input('Digite quantos termos deseja: '))

decimo = primterm + (Quantidade-1)*razao
for c in range(primterm,decimo,razao):
    print(c, end =' -> ')
print('Acabou')