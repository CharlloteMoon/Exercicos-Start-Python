print(f'{"Exercício 75":^40} \n{"ANÁLISE DE DADOS EM UMA TUPLA":^40} \n{"=" * 40}')
for c in range(1, 5):
    print('Digite o', end=' ')
    if c == 1:
        n1 = int(input(f'{c}º número: '))
    if c == 2:
        n2 = int(input(f'{c}º número: '))
    if c == 3:
        n3 = int(input(f'{c}º número: '))
    if c == 4:
        n4 = int(input(f'{c}º número: '))
nums = n1, n2, n3, n4
print(f'{"=" * 40} \nOs número digitados foram:', end=' ')
for num in nums:
    print(f'\033[1;33m{num}\033[m', end=' ')
print(f'\nO número \033[1;31m9\033[m apareceu \033[1;35m{nums.count(9)}\033[m vezes')
for num in nums:
    if num == 3:
        print(f'O número \033[1;31m3\033[m apareceu primeiro na \033[1;35m{nums.index(3) + 1}\033[mª posição')
print(f'Os números pares foram:', end=' ')
for num in nums:
    n = num % 2
    if n == 0:
        print(f'\033[1;32m{num}\033[m', end=' ')