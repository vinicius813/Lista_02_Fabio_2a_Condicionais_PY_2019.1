n1 = float(input('Submeta aqui a primeira nota do semestre: '))
n2 = float(input('Submeta aqui a segunda nota do semestre: '))
media = (n1 + n2) / 2
if media > 9 and media <= 10:
    print('Conceito A.')
elif media > 7.5 and media <= 9:
    print('Conceito B.')
if media > 6 and media <= 7.5:
    print('Conceito C.')
elif media > 4 and media <= 6:
    print('Conceito D.')
if media > 0 and media <= 4:
    print('Conceito E.')
elif media > 6 and media <= 10:
    print('APROVADO.')
if media > 0 and media <= 6:
    print('REPROVADO.')