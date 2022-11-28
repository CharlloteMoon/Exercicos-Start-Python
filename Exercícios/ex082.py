print(f'{" DESAFIO 82 ":^30} \n{" Dividindo Valores em Várias Listas ":^30} \n{"~" * 25}')

listavalores = []
listapares = []
listaimpares = []
pergunta = ' '
count = 0
total = 1

while pergunta not in 'N':
    while count != total:
        numero = int(input(f'Qual é o {count + 1}º valor? '))
        listavalores.append(numero)
        imparoupar = numero % 2
        if imparoupar == 0:
            listapares.append(numero)
        elif imparoupar == 1:
            listaimpares.append(numero)
        count += 1
    pergunta = str(input('Quer acrescentar mais valores(S/N)? ')).strip().upper()[0]
    if pergunta not in 'NS':
        print('Digite S para SIM  ou N para NÃO!')
    elif pergunta in 'S':
        total += 1
print('~' * 25)
print(f'''Os números digitados foram {listavalores}
Os números pares são {listapares}
Os números ímpares são {listaimpares}''')
