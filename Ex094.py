#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre: A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoas = [[]]
mulheres = []
acima = [[]]
pessoa = {}
c = soma = cont = pes=0
while True:
    pessoa[f'Pessoa {c}'] = {}
    if c != 0:
        pessoas.append([] * c)
    pessoa[f'Pessoa {c}']['nome'] = str(input('Nome:')).capitalize()
    while True:
        pessoa[f'Pessoa {c}']['sexo'] = str(input(f'Sexo[M/F]:'))[0].upper()
        if pessoa[f'Pessoa {c}']['sexo'] in 'MF':
            break
        print('Apenas M e F, tente novamente')

    pessoa[f'Pessoa {c}']['idade'] = int(input('Idade:'))
    pessoas[c].append(pessoa[f'Pessoa {c}'])
    c += 1
    while True:
        r = str(input('Quer continuar ?'))[0].upper()
        if r in 'SN':
            break
        print('Erro!!! Responda apenas [S/N]')
    if r in 'N':
        break

for k, v in pessoa.items():
    for i, y in pessoa[k].items():
        if i in 'idade':
            soma += y
            cont += 1
        if i in 'sexo' and 'f' in y:
            mulheres.append(pessoa[k]['nome'])

media = soma / cont
for k, v in pessoa.items():
    for i,y in pessoa[k].items():
        if pes != 0 :
            acima.append([]*pes)
        if i == 'idade' and y > media:
            acima[pes].append(pessoa[k]['nome'])
            acima[pes].append(pessoa[k]['sexo'])
            acima[pes].append(pessoa[k]['idade'])
            pes+=1

print('-=' * 20)

print(f'A média da idades deles é {media:2f}')
print('-*'*40)
print('as mulheres são:')
for i, v in enumerate(mulheres):
    print(v)
print('-*'*40)
print(f'As pessoas com a idade acima da média são : {acima}')

