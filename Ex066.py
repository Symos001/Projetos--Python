s=c=0
while True:
    n = float(input("Digite um número (999 para parar) :"))
    if n == 999 :
        parar = str(input("Deseja parar ?")).strip().upper()[0]
        if parar in "S":
            break
    c += 1
    s += n
print(f'A soma desses {c} valores foi {s}')