# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:

#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

tot18=toth=totm20=mulher=homem=dezoito=0
nomestot18 = []
nomestoth = []
nomestotm20 = []

while True:
    print("--"*15)
    print("Cadastre uma pessoa ")
    print("--"*15)

    nome = str(input("Nome : "))
    idade = int(input("Idade : "))
    sexo = ' '
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F] :")).strip().upper()[0]
    if idade > 18:
        tot18 += 1
        nomestot18.append(nome)
    if sexo == "M":
        nomeM= nome
        toth += 1
        nomestoth.append(nomeM)
    if sexo == "F" and idade < 20:
        totm20 += 1
        nomeF= nome
        nomestotm20.append(nomeF)
    continuar = ' '
    while continuar not in "SN":
        print("--" * 15)
        continuar = str(input("Quer continuar ?")).strip().upper()[0]
        print("--" * 15)
    if continuar == "N":
        break

print(f'''A quantidade de pessoas que tem mais de 18 anos é de {tot18}, e são respectivamente: {", ".join(nomestot18)}''')
print(f'''A quantidade de homens cadastrados foi de {toth}, sendo respectivamente: {", ".join(nomestoth)}''')
print(f'''A quantidade de mulheres que tem menos de 20 anos é de {totm20}, assim sendo: { ", ".join(nomestotm20)}''')
#print(f'''A quantidade de pessoas que tem mais de 18 anos é de {tot18}, e são respectivamente:''')
#for nome in nomestot18:
    #print(nome,end = ",")

#print(f'''A quantidade de homens cadastrados foi de {toth}, sendo respectivamente:''', end=' ')
#for nome in nomestoth:
    #print(nome,"," if len(nomestoth) > 1)

#print(f'''A quantidade de mulheres que tem menos de 20 anos é de {totm20}, assim sendo:''', end=' ')
#for nome in nomestotm20:
    #print(nome,',')

#print(f'''A quantidade de pessoas que tem mais de 18 anos é de {tot18}, e são respecitvamente {nomestot18}
#A quantidade de homens cadastrados foi de {toth}, sendo respectivamente {nomestoth}
# quantidade de mulheres que tem menos de 20 anos é de {totm20}, assim sendo {nomestotm20}''')
