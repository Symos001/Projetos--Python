# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

not50 = not20 = not10 = not1 = 0

print("="*40)
print("{:^40}".format("BANCO CEV"))
print("="*40)

while True:
    saque= int(input("Quanto deseja sacar ? R$"))
    totsaque= saque *1000

    if totsaque % 50 == 0:
       not50 = int(saque/50)
       saque -= (not50 * 50)
       print(F"Total de {not50} cédulas de R$50 ")

    if totsaque % 20 == 0:
        not20 = int(saque/20)
        if not20!= 0:
            print(f"Total de {not20} cédulas de R$20 ")
        saque -= (not20 * 20)

    if totsaque % 10==0:
        not10= int(saque/10)
        if not10 !=0:
            print(f"Total de {not10} cédulas de R$10")
        saque -= (not10 * 10)
    if totsaque % 1 == 0 :
        not1 = int(saque/1)
        if not1 != 0:
            print(f"Total  de {not1} cédulas de R$1")

    break

print("="*40)
print("BANCO CEV Agradece a sua visita ! Volte sempre!!!")








