#Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

#IMC = peso / (altura x altura).

peso = float(input('Digite seu peso (kg) :'))
altura = float(input('Digite sua altura(m) :'))
imc = peso / (altura**2)

print('Seu imc é equivalente a {:.1f} kg/m2'.format(imc))
if imc <= 18.5 :
    print('você esta ABAIXO do peso !')
elif 18.5 <= imc <= 25 :
    print('você está no peso IDEAL!')
elif 25 <= imc <= 30:
    print('você esta no SOBREPESO')
elif 30 <= imc <= 40:
    print('você esta com obesidade')
elif imc > 40:
    print('você esta com obesidade morbida')