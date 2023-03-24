#Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 parta viagens mais longas.
D= int(input('Digite a distancia da viagem : '))

if D <= 200 :
 print('Você deverá pagar {:.2f} , pois não passou de 200km'.format( D*0.5))
else:
 print('Você passou de 200km, deverá pagar {}'.format(D*0.45))