# Questão envolvendo percentagem de aumento salarial de empregados conforme Condicionais em parâmetro
antigo_salario = float(input('Escreva aqui seu salário bruto: R$ '))
# Colocar como parâmetro essa situação com vários if e elses
if antigo_salario <= 280:
    novo_salario_1 = (antigo_salario * 20/100) + antigo_salario
    print('Descrevendo o {:.2f} para reajuste 1'.format(novo_salario_1))
elif antigo_salario > 280 and antigo_salario <= 700:
    novo_salario_2 = (antigo_salario * 15/100) + antigo_salario
    print('Descrevendo o {:.2f} para o reajuste 2.'.format(novo_salario_2))
if antigo_salario > 700 and antigo_salario <= 1500:
    novo_salario_3 = (antigo_salario * 10/100) + antigo_salario
    print('Descrevendo o {:.2f} para o reajuste 3.'.format(novo_salario_3))
elif antigo_salario > 1500:
    novo_salario_4 = (antigo_salario * 5/100) + antigo_salario
    print('Descrevendo o {:.2f} para o reajuste 4.'.fortmat(novo_salario_4))
print('Com isso, está contratado!')



