#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

gols = []
dadosjog={}
dadosjog['gols']= list()


dadosjog['nome'] = str(input("Nome:"))
dadosjog['partidas'] = int(input("Quantas partidas:"))
for c in range(1,dadosjog['partidas']+1):
    gols =[ int(input(f"Quantos gols na {c}º partida:"))]
    dadosjog['gols'].append(gols[0])

print(f"O jogador {dadosjog['nome']}, jogou um total de {dadosjog['partidas']} partidas")
s=0
for i,v in enumerate(dadosjog['gols']):
    print(f'=> na partida {i+1}, ele fez {v} gols ')
    s+= v


print(f"Ele fez  um total de {s} gols")
