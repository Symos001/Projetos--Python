from random import randint
from time import sleep

print('vamos jogar JOKENPO !!')
sleep(2)
print('''Suas opções:
[1] pedra
[2] papel
[3] tesoura''')

usuario = int(input('Digite a sua escolha ?'))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(1, 3)

print('=*=' * 20)  # EFEITO VISUAL

if usuario == computador:  # Os dois escolhem a mesma coisa
    print('Ambos escolhemos o mesmo, deu EMPATE')

elif computador == 1:  # O computador joga pedra
    if usuario == 3:  # O usuário joga tesoura
        print('Você perdeu! eu joguei {}  e você jogou {}!'.format(itens[computador], itens[usuario]))
    elif usuario == 2:  # O usuário joga papel
        print('PARABENS!!Você ganhou escolheu {}, e eu escolhi {}'.format(itens[computador], itens[usuario]))

elif computador == 2:  # O computador joga papel
    if usuario == 1:  # O usuário joga pedra
        print('Você perdeu! eu joguei {}  e você jogou {}!'.format(itens[computador], itens[usuario]))
    elif usuario == 3:  # O usuário joga tesoura
        print('PARABENS!!Você ganhou escolheu {}, e eu escolhi {}'.format(itens[computador], itens[usuario]))

elif computador == 3:  # o computador joga tesoura
    if usuario == 1:  # O usuário joga pedra
        print('Você perdeu! eu joguei {}  e você jogou {}!'.format(itens[computador], itens[usuario]))
    elif usuario == 2:  # O usuário joga papel
        print('PARABENS!!Você ganhou escolheu {}, e eu escolhi {}'.format(itens[computador], itens[usuario]))
else:
    print('Jogada INVÁLIDA')
print('=*=' * 20)  # EFEITO VISUAL
