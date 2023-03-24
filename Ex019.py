import random

n1 = input('Digite um nome')
n2 = input('Digite outro nome')
n3 = input('Digite outro nome')
n4 = input('Digite outro nome')
Lista= [n1,n2,n3,n4]
result = random.choice(Lista)
print('O aluno escolhido é {}'.format(result))
