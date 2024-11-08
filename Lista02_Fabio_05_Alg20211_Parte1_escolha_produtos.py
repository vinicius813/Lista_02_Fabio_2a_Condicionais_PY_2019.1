preco_1 = float(input('Digite aqui o preço do produto 1: '))
preco_2 = float(input('Digite aqui o preço do produto 2: '))
preco_3 = float(input('Digite aqui o preço do produto 3: '))
if preco_1 < 6.45:
    print('Este produto deve ser comprado na Terça-feira.')
elif preco_2 >= 12.80:
    print('Este produto está sobrando no estoque.')
else:
    print('Vou comprar! Opte pelo mais barato.')