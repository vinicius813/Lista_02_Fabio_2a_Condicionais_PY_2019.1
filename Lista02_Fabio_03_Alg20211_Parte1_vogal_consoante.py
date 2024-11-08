vogais = ['a', 'e', 'i', 'o', 'u']
letra = input('Digite aqui uma letra do nosso Alfabeto: ')
if letra in vogais:
    print('É uma vogal.')
elif letra.isalpha():
    print('É uma consoante.')
else:
    print('Nem vogal nem consoante.')
