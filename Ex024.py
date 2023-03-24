# Crie um programa que leia o nome de uma cidade
# diga se ela começa ou não com o nome “SANTO”.
cid = str(input('Digite o nome de sua cidade : ')).strip()
sep = cid.upper().split()
print("SANTO" in sep[0])
