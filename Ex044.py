#Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros
print('='*40)
print('{:=^40}'.format(' LOJAS ROSSI    '))
print('='*40)
valor = float(input('Digite o valor do pagamento:'))
print('COMO DESEJA PAGAR ? ')

print('[1] à vista dinheiro/cheque')
print('[2] à vista no cartão')
print('[3] em até 2x no cartão')
print('[4] em 3x ou mais no cartão')

modpag = int(input('Digite o modo de pagamento:'))


if modpag == 1:
    print('o valor deste produto será de {}'.format((valor - valor *10) / 100))
elif modpag == 2 :
    print('o valor deste produto será de {}'.format((valor - valor * 5) / 100))
elif modpag == 3:
    print('o valor deste produto será de duas parcelas de R${}'.format(valor/2))

elif modpag == 4:
        parcelas = int(input('Em quantas vezes ?'))
        juros20 = valor + (valor *20 / 100)
        total = (juros20/parcelas)
        print (' o valor no produto em {} vezes no cartão ,'.format(parcelas),end=' '
                  'será de R${:.2f} por parcela,')
        print('sendo assim sua compra de R${},terá como valor final de R${}'.format (total ,valor, juros20))

