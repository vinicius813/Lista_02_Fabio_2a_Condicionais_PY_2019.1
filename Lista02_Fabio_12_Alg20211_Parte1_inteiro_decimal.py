numero_decimal = float(input('Digite aqui um número decimal: '))
numero_inteiro = int(input('Digite aqui um número inteiro: '))
# Um número é inteiro se  quando multiplicado por um for ele mesmo ou maior igual a 1 é inteiro.
# Decimal caso seja maior ou igual a 1 e menor que -1
resolucao = (numero_decimal * 1) + (numero_inteiro ** 0)
if resolucao >= 1 or resolucao < -1:
    print('Logo, ele é um {:.1f} número inteiro.'.format(resolucao))
else:
    print('Logo, ele é um {:.1f} número de ponto flutuante/decimal.'format(resolucao))