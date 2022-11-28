print('--- EXERCICIO 48 --- \n SOMA DE ÍMPARES MULTIPLOS DE TRÊS')
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
        print(c, end=', ')
print(f'\nA soma dos {cont} números ímpares multiplos de 3 é {soma}.')
