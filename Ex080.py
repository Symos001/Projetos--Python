# Crie um programa onde o usuário possa
# digitar cinco valores numéricos e cadastre-os
# em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.
cont=0
num = []
for c in range(0, 5):
    n = int(input("Digite um numero:"))

    if c ==0 or n > num[len(num)-1]:
        num.append(n)
    else:
        pos=0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos,n)
                break
            pos+=1


print('-='*30)
print(f'Os valores digitados em ordem foram {num}')






