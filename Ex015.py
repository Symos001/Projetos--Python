v= float(input('velocidade em Km'))
d= int(input('quantidade de dias que ele viajou'))
F = (v*0.15)+(d*60)
print('o valor total a se pagar é R$ {:.2F}'.format(F))