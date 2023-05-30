
#Exercício Python 090: Faça um programa que leia nome
# e média de um aluno, guardando também a situação
# em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno1={}
aluno1['Nome']=str(input('Nome do aluno:'))
aluno1['Média']=float(input(f'Média de {aluno1["Nome"]}:'))
if aluno1['Média'] >= 7:
    aluno1['Situação'] = 'APROVADO!!'
elif 5 <= aluno1['Média'] < 7:
    aluno1['Situação'] = 'RECUPERAÇÃO'
else:
    aluno1['Situação'] = 'REPROVADO!! :('
for k,v in aluno1.items():
    print(f'{k} é igual a {v}')
print(f'O {aluno1["Nome"]},esta  de {aluno1["Situação"]}')