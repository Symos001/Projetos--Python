Nome = str(input("diga seu nome completo")).strip()
Sep = Nome.split()

print('Analizando...')
print('Seu nome com todas as letras maiusculas é {}'.format(Nome.upper()))
print('seu nome com todas as letras minusculas é {}'.format(Nome.lower()))
print('A quantidade de letras em seu nome é {}'.format(len(Nome) - Nome.count(' ')))
print('O seu  primeiro nome é {} , quantidade de letras  nele é {}'.format(Sep[0], Nome.find(' ')))
