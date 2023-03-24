n1= float(input('Quanto mede a altura de sua parede ?'))
n2= float(input('Quanto mede a largura de sua parede?'))
A= n1*n2
L= A/2
print('A sua parede tem a dimensão de {}x{}, e sua sua area é de {} m2,'.format(n1,n2,A))
print(' sendo necessário uma quantidade de {} litros para pinta-la'.format(L))
