import math
cato= float(input('digite o numero do cateto oposto'))
cata= float(input('digite o numero do cateto adjascente'))
hip= math.hypot(cato,cata)
print('o valor da hipotenusa é {}'.format(hip))