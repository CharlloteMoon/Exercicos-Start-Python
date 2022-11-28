n = input('Digite algo: ')
print('É uma variavel tipo {}' .format(type(n)))
print('É um número? ({})' .format(n.isnumeric()))
print('É uma letra? ({})' .format(n.isalpha()))
print('É uma letra com número? ({})'.format(n.isalnum()))
print('Está em maiuscula? ({})' .format(n.isupper()))
print('Está em minuscula? ({})'.format(n.islower()))

