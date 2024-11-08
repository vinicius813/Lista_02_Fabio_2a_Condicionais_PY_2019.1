# Leitura de casas decimais
n1_secreto = int(input('Escreva um número menor que 1000: '))
centenas = n1_secreto // 100
dezenas = (n1_secreto % 100) // 10
unidades = (n1_secreto % 10) // 1
# A questão pede uma mistura de definiçâo de função com estruturas condicionais em Python

def verifica_centena():
    if centenas == 1:
        return 'centena'
    else:
        return 'centenas'

def verifica_dezena():
    if dezenas == 1:
        return 'dezenas'

def verifica_unidade():
    if unidades == 1:
        return 'unidade'
    else:
        return 'unidades'

    if n1_secreto // 100 != 0:
    if n1_secreto % 100 == 0:
    print(f'{n1_secreto} = {centenas} {verifica_centena()}')

    elif n1_secreto % 100 != 0:
    if n1_secreto % 10 == 0:
    print(f'{n1_secreto} = {centenas} {verifica_centena()} e' f'{dezenas} {verifica_dezena()}')

    elif n1_secreto % 10 != 0:
    print(f'{n1_secreto} = {centenas} {verifica_centena()},' f'{dezenas} {verifica_dezena()} e' f'{unidades} {verifica_unidade()}')

    elif n1_secreto // 100 == 0:
    if n1_secreto >= 10:
    if n1_secreto % 10 == 0:
    print('f{n1_secreto} {dezenas} {verifica_dezena()}')

    elif n1_secreto % 10 != 0:
    print(f'{n1_secreto} = {dezenas} {verifica_dezena()} e' f'{unidades} {verifica_unidade()}')

    else:
    print(f'{n1_secreto} = {unidades} {verifica_unidade()}')


