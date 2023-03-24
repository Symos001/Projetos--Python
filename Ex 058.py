import random
import time

cont = 0
cont2 = 0
cont3 = 0
jog = 0
print('-+-' * 10)
print('JOGO DE ADIVINHAÇÃO V2')
print('-+-' * 10)
time.sleep(1)
print('    ')
print('Pensarei em um numero de 0 a 5, tente adivinhar')
print('     ')
time.sleep(1)
comp = random.randint(0, 5)  # computador pensa em um numero

while jog != comp: #o jogador irá dar o palpite e se for diferente o jogador tera que jogar de novo
    jog = int(input('Digite seu palpite:')) #Palpite do jogador
    print('ANALISANDO...')
    time.sleep(2)
    cont += 1
    if jog > comp: #se o palpite for maior que numero do computador
        print('Você errou é um pouco menor,tente de novo')

    elif jog < comp:#se o palpite for menor que o do computador
        print('Você errou é um pouco maior, tente de novo')

if cont > 1: #se a quantidade de laços for maior que 1
    print('Parabens você acertou!! Você levou {} palpites, para acertar !!'.format(cont))
if cont == 1: #se a quantidade de laços for igual a 1
    print('Meus parabens!! acertou de primeira, eu estava pensando em {}'.format(comp))
