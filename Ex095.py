# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogadores = []
jog = {}
jog['gols'] = []
while True:
    jog = {}
    jog['nome'] = str(input("Nome do jogador:"))
    jog['partidas'] = int(input("Quantas partidas:"))
    jog['gols'] = []
    for c in range(1, jog['partidas']+1):
        gols = int(input(f"Quantos gols na {c}º partida:"))
        jog['gols'].append(gols)
    jog['totgols'] = sum(jog['gols'])
    jogadores.append(jog)
    while True:
        r = str(input('Quer continuar ?'))[0].upper()
        if r in 'SN':
            break
        print('Erro!!! Apenas [S/N] ')
        
    if r in 'N':
        break

for i, jog in enumerate(jogadores):
    print('=-'*40)
    print(f"O jogador {jog['nome']}, jogou um total de {jog['partidas']} partidas")
    for j, gols in enumerate(jog['gols']):
        print(f'=> na partida {j + 1}, ele fez {gols} gols ')

    print(f"Ele fez  um total de {jog['totgols']} gols")
