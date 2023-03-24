# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

cont1 = 0
cont2 = 0
cont3 = 0
for c in range(1, 8):

    cont1 += 1
    dn = int(input('Digite o ano de nascimento {}º pessoa : '.format(cont1)))
    hoje = date.today().year
    dif = hoje - dn
    if  dif >= 21 :
        cont2 +=1
    else :
        cont3 +=1

print('Ao todo temos {} pessoas maiores de idade, e {} pessoas menores de idade'.format(cont1,cont3))


