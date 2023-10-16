# 079
# Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

listan = []
while True:
    n = int(input("Digite um valor:"))
    if n not in listan:
        listan.append(n)
        print("Adicionado com sucesso")
    else:
        print("Valor duplicado, não será adicionado ")
    r = str(input('Quer continuar ?'))[0].strip().lower()
    if 'n' in r:
        break
listan.sort()
print(f"Todos os valores unicos digitados foram {listan}")

