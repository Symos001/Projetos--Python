#A Confederação Nacional de Natação precisa de um programa
# que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade
# Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

from datetime import date
ano = int(input('Digite o ano de nascimento do atleta :'))
idade = date.today().year - ano
print('Esse atleta tem {} anos '.format(idade))
if idade <= 9 :
    print('A categoria deste atleta é MIRIM')

elif idade <= 14 :
    print('A categoria desse atleta é INFANTIL')

elif idade <= 19 :
    print('A categoria desse atleta é JÚNIOR')

elif idade <= 25 :
    print(' A categoria desse atleta é SÊNIOR')

else:
    print('A categoria desse atleta é MASTER')
