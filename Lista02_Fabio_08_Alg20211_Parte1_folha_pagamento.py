# O cálculo para uma folha de pagamento com descontos de I.R por tabela
valor_hora = float(input('Digite aqui o valor da hora de uma empresa: '))
quant_horas = int(input('Digite aqui o número de horas trabalhadas: '))
salario_bruto = float(input('Coloque na ponta do lápis o seu salário bruto: R$ '))
# Parâmetro desta vez são leituras de 3 valores de um Sindicato para calcular o subTotal de I.R
salario_liquido = (valor_hora * quant_horas) + salario_bruto
print('Colocando na ponta do lápis, seu salário liquido sem dedução de impostos é de {:.2f}'.format(salario_liquido))
if salario_bruto <= 900:
    print('Apresento-lhe uma situação hipotética de valores sem dedução de impostos.')
    print('Isento de imposto.')
elif salario_bruto > 900 and salario_bruto <= 1500:
    novo_imposto_2 = (salario_bruto * 5/100) - salario_liquido
    print('Desconto de 5% no I.R levará a {:.2f}'.format(novo_imposto_2))
if salario_bruto > 1500 and salario_bruto <= 2500:
    novo_imposto_3 = (salario_bruto * 10/100) - salario_liquido
    print('Desconto de 10% no I.R levará a {:.2f}'.format(novo_imposto_3))
elif salario_bruto > 2500:
    novo_imposto_4 = (salario_bruto * 20/100) - salario_liquido
    print('Descontão de 20% no I.R levará a {:.2f}'.format(novo_imposto_4))
else:
    print('Bom dia! Siga em frente!')

