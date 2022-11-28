print(f'\033[1;36m{" Exercício 86 e 87 ":-^30}\033[m \n{" Matriz em Python ":^30}')

numeros = []
matriz = [[], [], []]
par = []
terceiracoluna = []

print(f'\n{"-" * 30}')

for p in range(0, 3):
    for c in range(0, 3):

        numeros.clear()

        numeros.append(int(input(f'Valor ({p}, {c}): ')))

        matriz[p].append(numeros[:])

        if matriz[p][c][0] % 2 == 0:
            par.append(numeros[:])

        if c == 2:
            terceiracoluna.append(numeros[:])

print(f'\n{"-" * 30}')

for p in range(0, 3):

    for c in range(0, 3):
        print(f'[{matriz[p][c][0]:^5}]', end='    ')

        if c == 2:
            print('\n', end='')

soma3coluna = soma = maxnum = 0

for c in range(0, len(terceiracoluna)):
    soma3coluna += terceiracoluna[c][0]

for c in range(0, len(matriz[1])):
    if maxnum < matriz[1][c][0]:
        maxnum = matriz[1][c][0]

for c in range(0, len(par)):
    soma += par[c][0]

print(f'''\n{"-" * 30}
A soma de todos os valores pares é igual a {soma}.
A soma dos valores da terceira coluna é igual a {soma3coluna}.
O maior número da segunda coluna é igual a {maxnum}.''')
