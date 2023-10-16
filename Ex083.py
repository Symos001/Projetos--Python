# Crie um programa onde o usuário
# digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada
# está com os parênteses abertos e fechados na ordem correta.

cont=0
while True:# a estrutura de de controle faz a validadação do resultado
           # até o usuário usuario digitar corretamente a expressão

    cont+=1
    n = input("Digite a sua expressão: ")
    ex = (list(n)) # essa tupla , é a expressão separada por caracter
    parA = [] #essa lista é dos  parenteses ')'
    parB = [] #essa lista é dos parenteses '('

    for i, v in enumerate(ex):#essa estrutura de controle verifica os parenteses
                              # e separa eles em listas
        if v in ')':
            parA.append(v)
        elif v in '(':
            parB.append(v)

    if len(parA) != len(parB): #se a quantidade de parenteses ')'
                               # não for a mesma que a quantidadde de parentese '('
                               # e dependendo de quantas você digitou ele
                               # irá dar uma dica de quantos parentese faltam
        print('Você não digitou a expressão da maneira correta, utilize os parenteses')
        if cont > 1:
            print('faltam ',end='')
            print(len(parA)-len(parB) if parA>parB else len(parB)-len(parA),end=' ')
            print('parenteses')
    elif len(parA) == len(parB) and n != '': #se a quantidade for igual , a expressão está certa
        print('Você digitou a expressão corretamente')
        break

print(f'A expressão que você digitou foi : {n}') #mostra a expressão novamente
