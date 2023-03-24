# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input('Me diga, em que ano você nasceu ?'))
hoje = date.today().year
diferenca = int(hoje - ano)

ano1 = int(18 + ano)

if diferenca == 18:
    print('Você já esta no tempo de se alistar no exercito!')


elif diferenca > 18:
    print('Vish, você ja deveria ter se alistado h a {} anos em {}'.format(diferenca - 18, ano1))

else:
    print('Voce ainda vai se alistar daqui há {} anos no ano de {} '.format(18 - diferenca, ano1))
