# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:

# – Média abaixo de 5.0: REPROVADO

# – Média entre 5.0 e 6.9: RECUPERAÇÃO

# – Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite o valor de sua primeira nota :'))
nota2 = float(input('Digite o valor de sua segunda nota :'))
media = float(nota1 + nota2) / 2

if media < 5:
    print('Você tirou {} e {}, obtendo a média {},  não atingiu a pontuação necessária , você esta REPROVADO'.format(nota1, nota2, media))
    print()

elif media >= 7:
    print('Parabens você teve as notas {} e {}, obtendo a média {}, você foi APROVADO!'.format(nota1,nota2,media))

elif media > 5 and media < 7:
    print('Você teve as notas {} e {} , obtendo a média {}, não atingiu a pountuação ideal, você esta de RECUPERAÇÃO')
