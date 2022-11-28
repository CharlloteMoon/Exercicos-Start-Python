print(f'{" DESAFIO 80 ": ^30} \n{" Lista Ordenada sem Repetições ": ^30} \n{"~":~^25}')

listanumeros = []

for c in range(1, 6):
    numero = int(input(f'Digite o {c}º valor: '))
    if c == 1:
        print(f'O número {numero} foi adicionado na posição 0.')
        listanumeros.append(numero)
    elif c == 2:
        if numero < listanumeros[0]:
            print(f'O número {numero} agora está na posição 0')
            listanumeros.insert(0, numero)
        elif numero > listanumeros[0]:
            print(f'O número {numero} agora está na última posição.')
            listanumeros.insert(1, numero)
    elif c == 3:
        if numero < listanumeros[0]:
            print(f'O número {numero} agora está na posição 0.')
            listanumeros.insert(0, numero)
        elif numero < listanumeros[1]:
            print(f'O número {numero} agora está na posição 1.')
            listanumeros.insert(1, numero)
        elif numero > listanumeros[1]:
            print(f'O número {numero} agora está na última posição.')
            listanumeros.insert(2, numero)
    elif c == 4:
        if numero < listanumeros[0]:
            print(f'O número {numero} agora está na posição 0.')
            listanumeros.insert(0, numero)
        elif numero < listanumeros[1]:
            print(f'O número {numero} agora está ba posição 1.')
            listanumeros.insert(1, numero)
        elif numero < listanumeros[2]:
            print(f'O número {numero} agora está na posição 2.')
            listanumeros.insert(2, numero)
        elif numero > listanumeros[2]:
            print(f'O número {numero} agora está na última posição')
            listanumeros.insert(3, numero)
    elif c == 5:
        if numero < listanumeros[0]:
            print(f'O número {numero} agora está na posição 0.')
            listanumeros.insert(0, numero)
        elif numero < listanumeros[1]:
            print(f'O número {numero} agora está na poisção 1.')
            listanumeros.insert(1, numero)
        elif numero < listanumeros[2]:
            print(f'O número {numero} agora está na posição 2.')
            listanumeros.insert(2, numero)
        elif numero < listanumeros[3]:
            print(f'O número {numero} agora está na posição 3.')
            listanumeros.insert(3, numero)
        elif numero > listanumeros[3]:
            print(f'O número {numero} agora está na última posição.')
            listanumeros.insert(4, numero)
print('~' * 25)
print(f'Os números digitados foram {listanumeros}')
