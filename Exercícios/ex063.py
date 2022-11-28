print('--- EXERCICIO 63 --- \n SEQUÊNCIA DE FIBONACCI v1.0')
n = int(input('Quantos termos você quer ver? '))
ultimo = 1
penultimo = 1
if n == 1:
    print('1')
elif n == 2:
    print('1 -> 1')
else:
    count = 3
    print(f'{penultimo} -> {ultimo} ->', end=' ')
    while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        if count < n:
            print(f'{termo} ->', end=' ')
        elif count == n:
            print(f'{termo}')
        count += 1
