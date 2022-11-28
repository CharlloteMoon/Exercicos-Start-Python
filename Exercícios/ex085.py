print(f'\033[1;36m{f" Exercício 85 ":-^30}\033[m \n{" Listas de Pares e Ímpares ":^30}')

numero = []
parEImpar = [[], []]

for c in range(1, 8):

    numero.clear()

    print(f'\n{f" {c}º Valor ":-^30}')
    numero.append(int(input('Digite o valor: ')))

    if numero[0] % 2 == 0:
        parEImpar[0].append(numero[:])
    else:
        parEImpar[1].append(numero[:])

print(f'''\n{"-" * 30}
Os números pares digitados foram ''', end='')

for p in sorted(parEImpar[0]):
    print(f'\033[1;35m{p[0]}\033[m', end=' ')

print()

print('Os números ímpares foram ', end='')

for p in sorted(parEImpar[1]):
    print(f'\033[1;36m{p[0]}\033[m', end=' ')

print()
