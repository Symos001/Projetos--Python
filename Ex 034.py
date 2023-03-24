#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
s = float(input('Diga o seu salário :'))
au10 = s + s*10/100
au15 = s + s*15/100
if s > 1200.00:
    print('Com o aumento de 10% seu salário é R$ {}'.format(au10))
if s <= 1200.00:
    print('Com o aumento de 15% o seu salário será de R$ {}'.format(au15))
