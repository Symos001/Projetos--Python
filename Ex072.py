
import time
Numeros = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis' ,
           'sete', 'oito', 'nove', 'dez','onze','doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dessete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        num = int(input( 'Digite um numero entre 0 e 20:'))
        if 0 <= num <= 20:
            break
        print('Tente novamente', end =', ')
    print(f'Você digitou o número {Numeros[num]}')
    time.sleep(1)
    r = str(input("Quer continuar ?[S/N]"))[0].strip().lower()
    if r in 'n':
        break