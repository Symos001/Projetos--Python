import math
Ang= int(input('Digite um angulo'))
sen= math.sin(math.radians(Ang))
cos= math.cos(math.radians(Ang))
tang= math.tan(math.radians(Ang))

print('o valor do seno {:.2f}'.format(sen))
print('o valor do coseno {:.2f}'.format(cos))
print('o valor da tangente {:.2f}'.format(tang))