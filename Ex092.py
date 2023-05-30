#Exercício Python 092: Crie um programa que leia nome, ano de nascimento
# e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também
# o ano de contratação e o salário. Calcule e acrescente, além da idade,
# com quantos anos a pessoa vai se aposentar.

from datetime import date
trabalhadores = {}
hoje = date.today().year
print(hoje)
trabalhadores['Nome'] = str(input('Nome:')).strip()
trabalhadores['Idade'] = int(input('Ano de nascimento:'))
trabalhadores['CTPS'] = int(input('Carteira de trabalho (0 caso não tem):'))
cont=0
if trabalhadores['CTPS'] != 0:
    trabalhadores['Ano de contratação'] = int(input('Ano de contratação:'))
    trabalhadores['Salário'] = float(input('Salário:'))

trabalhadores['Aposentadoria'] = (trabalhadores['Ano de contratação'] + 35) - trabalhadores['Idade']
trabalhadores['Idade'] = hoje - trabalhadores['Idade']
print('-='*30)
for k,v in trabalhadores.items():
    print(f'O {k} tem valor {v}')


