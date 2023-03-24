print("+="*20)
print("Progressão aritimética V3.O ")
print("+="*20)
p: int= int(input("Digite o primeiro termo:"))
r= int(input("Digite a razão : "))
termo = p
c = 1
mais = 10
total = 0
vic=0
print(p ,'->',end='')
while mais != 0:
    total= total + mais
    while c != total:
        termo +=r
        c +=1
        print('{}->'.format(termo) , end= '')
    print('PAUSA ')
    mais = int(input('Quanto termos quer mostrar a mais ?'))
print('Progressão finalizada com {} termos'.format(total))
