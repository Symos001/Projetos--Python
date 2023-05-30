#Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex:
# escreva(‘Olá, Mundo!’) Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~

def escreva(msg):
    esp= len(msg)+4
    print('~'*esp)
    print(' '*2,end='')
    print(msg)
    print('~'*esp)


#Programa Prncipal
escreva('Batatas Cozidas ao molho')
