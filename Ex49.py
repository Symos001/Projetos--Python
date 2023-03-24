
#Refaça o DESAFIO 9,
# mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.
n1 = int(input('Digite um numero :'))
for c in range(1,11):
    resultado = c*n1
    print('{} x {} = {}'.format(n1,c,resultado))