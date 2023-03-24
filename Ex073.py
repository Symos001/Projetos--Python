times= ('América FC' , 'Atletico Mineiro','Bota Fogo','Atletico Paranaense',
        'Coritiba', 'Flamengo','Vasco da Gama','Cruzeiro','Cuiaba','Bahia',
        'Fluminense','Fortaleza','Goias','Gremio', 'Bragantino','Santos','São Paulo',
        'Corintians', 'Internacional', 'Palmeiras')

cont=0
#Mostra os cinco primeiros
print( f"Os cinco primeiros times da tabela são {times[0:5]}")
#Os ultimos quatro colocados da tabela
print(f"Os quatro ultimos colocados da tabela são {times[16:21]}")
#Lista dos times em ordem alfabética
for c in times:
    if  "A" in c[0][0] :
        print(c)
    elif "B" in c[0][0]:
        print(c)
    elif "C" in c[0][0]:
        print(c)
    elif "F" in c[0][0]:

#Lugar em que o time do palmeiras está
if times == 'Palmeiras ':
    print(f'O Palmeiras esta ná {}')
