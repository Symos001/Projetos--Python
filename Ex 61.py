#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
p: int= int(input("Digite o primeiro termo:"))
r= int(input("Digite a razão : "))
termo = p
c = 1
print(p ,'->',end='')
while c != 10:
    termo +=r
    c +=1
    print('{}'.format(termo),'->' if c<10  else "  FIM ", end= '')
