# Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.


s = str(input('Digite seu sexo [M/F]:')).strip().upper()[0]
F= 'Feminino'
M= 'Masculino'
while s not in 'MF':
    if s != 'M' or s != 'F':
        s = str(input('Dados invalidos por favor informe o seu sexo: ')).strip().upper()
if s == 'M':
    s = M
else:
    s = F
print('Sexo {}, registrado com sucesso'.format(s))
