# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
# mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

cont2 = 0
cont3 = 0
lista = []
lista2 = []
media = 0
maisvelho = 0
nomevelho = 0
igual = 0

for p in range(1, 5):
    print('-' * 19)
    print('-' * 4, '{}º pessoa'.format(p), '-' * 4)
    print('-' * 19)
    nome = str(input('Digite seu nome :')).strip()
    idade = int(input('Digite a sua idade :'))
    sexo = str(input('Digite seu sexo :')).strip()
    sep = nome.split()
    cont2 += 1

    if cont2 >= 1:
        lista.append(idade)  # Coloca as idades numa lista

    if p == 1 and sexo in 'Mm':  # identifica e tranforma a variavel maisvelho e nomevelho em variaveis que
        # foram adicionadas  no laço
        maisvelho = idade
        nomevelho = nome
        igual += 1

    if sexo in 'Mm' and idade > maisvelho:  # se a idade for maior que anterior, ou seja, maior que um
        # ela vai receber o nome da variavel mais velha e contar um
        # para identificar se houve ou não uma pessoa mais velha
        maisvelho = idade
        nomevelho = nome
        igual += 1


    elif sexo == 'feminino' or sexo == 'f':  # Identifica se uma mulher tem mais de 20 anos ou não
        if idade < 20:
            cont3 += 1
            lista2.append(nome)

media = sum(lista) / 4  # calcula a média

print(' ' * 100)

if igual >= 1:  # Mostra o homem mais velho
    print('1- O homem mais velho é  {} , com a idade de {} anos '.format(nomevelho, maisvelho))

elif igual == 0:  # e se todos estivem com a mesma idade mostra qie todos tem a mesma idade
    print('1-Todos tem a mesma idade ')

print(' ' * 100)

if cont3 == 0:  # Se nenhuma menina tiver menos de 20 anos mostra isso
    print('2-Temos um total de 0 meninas menores que 20 anos ')

else:  # Mostra quantas e quais meninas tem menos de 20 anos
    print('2-A quantidade de mulheres que tem menos de 20 anos, é igual a {},'.format(cont3))
    print('Sendo que apenas {} que tem menos de 20 anos '.format(lista2))

print(' ' * 100)

print('3-A media  de idades é igual a {} '.format(media))  # Mostra a media de idade deles
