print('--- EXERCICIO 53 --- \n DETECTOR DE PALÍNDROMO')
n = str(input('Digite uma frase: '))
nao = str(n)[: :-1]
print('A frase {} ao contrária é {}' .format(n.title(), nao.title()))
if str(n) == str(n)[: : -1]:
    print('A frase é PALÍNDROMA!')
else:
    print('A frase NÃO é PALÍNDROMA!')
