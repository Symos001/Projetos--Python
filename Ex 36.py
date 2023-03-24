# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
v = float(input('Qual é o valor da casa ?'))
s = float(input('Qual é o seu salário ?'))
a = int(input('Em quantos anos pretende pagar ?'))
conv = a * 12  # converte anos em meses
conta = v / conv  # dá o quanto deverá se pago por mes

if conta >= s * 30 / 100:  # dá a condição e calcula se o valor da parcela é superior a 30% do salário
    print('Para uma casa que vale R$ {}, em {} anos terá uma prestação de R${:.2f} por mês'.format(v, a, conta))
    print('sendo esse um valor superior a 30% do seu salário , seu emprestimo foi NEGADO')

elif conta < s * 30 / 100:  # dá a condição e calcula se o valor da parcela é inferior a 30% do salário
    print('Para uma casa que vale R$ {}, em {} anos terá uma prestação de R$ {:.2f} por mês'.format(v, a, conta))
    print('sendo esse um valor inferior a 30% do seu salário, seu emprestimo foi APROVADO')
