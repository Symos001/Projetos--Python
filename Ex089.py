#Exercício Python 089: Crie um programa que leia nome e
# duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um
# e permita que o usuário possa mostrar as notas de cada aluno individualmente.

cadast=[[]]
n=cont=media=0
while True:
    nome = str(input('Digite seu nome:'))
    n1 = float(input('Digite a sua primeira nota:'))
    n2 = float(input('Digite a sua segunda nota:'))
    media = (n1+n2)/2
    cadast[cont].append(nome)
    cadast[cont].append(n1)
    cadast[cont].append(media)
    cont+=1
    cadast.append([])
    r = str(input('Quer continuar ?'))[0].upper()
    n+=1
    if r in 'Nn':
        break
print('No.', end=' ')
print('NOME',end='')
print(' '*10,end=' ')
print('MEDIA')
print('-'*30)
for c in range(0,n):
    print(c,end=' ')
    print(f'  {cadast[c][0]}',end=' ')
    print(len(cadast[c][0]),end='')
    print(' ' * 10 , end=' ')
    print(f'  {cadast[c][2]}')

