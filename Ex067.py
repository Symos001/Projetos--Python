while True:
    n = int(input("Digite um número real para conferir a TABUADA:"))
    print('-' * 47)
    if n < 0 :
        break
    for c in range(1, 11):
        t= n*c
        print(f"{n} X {c} = {t}")
    print('-'*47)
print("Programa Tabuada ENCERRADO!!")
