import random
n1= input('nome do primeiro aluno')
n2= input('nome do segundo aluno')
n3= input('nome do terceiro aluno')
n4= input('nome do quarto aluno')
lista= [n1,n2,n3,n4]
esc1= random.shuffle(lista)
print('a ordem alunos a apresentar  será {}'.format(lista))