
import time
import random
cont= 0
print('-+-'*10)
print("BEM VINDO")
time.sleep(1)
print("VAMOS JOGAR PAR OU IMPAR ")
time.sleep(1)
print("-+-"*10)
while True:
    jog = int(input("Digite seu numero:"))
    pc = random.randint(0, 11)
    soma = pc + jog
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I] ?')).strip().upper()[0]
    print("Vamos lá!!!")
    time.sleep(1)
    print("PAR")
    time.sleep(1)
    print("OU")
    time.sleep(1)
    print("IMPAR")
    print(f"Você jogou {jog} e o computador jogou {pc} .Total de {soma}", end=' ')
    print('DEU PAR' if soma % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if soma %2 ==0:
            print(f"Você VENCEU! ")
            cont =+1
        else:
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print(f"Você VENCEU!")
            cont =+1
        else:
            print(f"Você PERDEU!")
            break
    print('Vamos jogar novamente')
print(f"GAME OVER , você venceu {cont} vezes")
