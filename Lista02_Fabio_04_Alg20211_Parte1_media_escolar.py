n1 = float(input('Digite aqui a primeira nota: '))
n2 = float(input('Digite aqui a segunda nota: '))
media = (n1 + n2) / 2
print('A sua média foi {:.2f}'.format(media))
if media >= 7:
    print('APROVADO!! Parabéns, você alcançou a tão sonhada aprovação.')
elif media <= 7:
    print('REPROVADO!! Estude mais na próxima!')
if media == 10:
    print('Aprovado com Distinção.')