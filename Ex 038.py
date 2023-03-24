# Escreva um programa que leia dois números inteiros e compare-os.
# mostrando na tela uma mensagem:
# – O primeiro valor é maior

# – O segundo valor é maior

# – Não existe valor maior, os dois são iguais

num1 = int(input('Digite um numero inteiro :'))
num2 = int(input('Digite um numero inteiro :'))
if num1 > num2:
    print('O numero {}, é maior !'.format(num1))
elif num2 > num1:
    print('O numero {}, é maior !'.format(num2))

elif num2 == num1 :
    print('Não existe valor maior , os dois são iguais')
