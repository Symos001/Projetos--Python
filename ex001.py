nome = input('qual é o seu nome?')
Cores = {'limpa': '\33[m',
         'vermelho': '\33[31m',
         'azul ': '\33[34m',
         'amarelo ': '\33[33m'}

print('é um prazer te conhecer {}{}{}!!!'.format(Cores['azul '], nome, Cores['limpa']))
