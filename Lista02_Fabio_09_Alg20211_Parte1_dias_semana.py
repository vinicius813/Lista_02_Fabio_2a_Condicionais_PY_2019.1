numero = ['1', '2', '3', '4', '5', '6', '7']
dias_semana = input('Diga um número que corresponda a um dia da semana: '.format(numero))
if '1' in dias_semana:
    print('Domingo.')
elif '2' in dias_semana:
    print('Segunda-Feira.')
elif '3' in dias_semana:
    print('Terça-Feira.')
elif '4' in dias_semana:
    print('Quarta-Feira.')
elif '5' in dias_semana:
    print('Quinta-Feira.')
elif '6' in dias_semana:
    print('Sexta-Feira.')
elif '7' in dias_semana:
    print('Sábado.')
else:
    print('Valor inválido.')