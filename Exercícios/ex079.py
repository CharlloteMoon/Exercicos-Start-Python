print(f'{" Exercício 79 ":-^30} \n{" Valores Únicos em uma Lista ":^30} \n{"-" * 30}')

listavalores = []
pergunta = ' '
count = 0
total = 1

while pergunta not in 'N':
    while count != total:
        numero = int(input('Quer adicionar qual número? '))
        if numero not in listavalores:
            listavalores.append(numero)
            count += 1
        else:
            print('Número já adicionada, tente outro número')
    pergunta = str(input('Quer acrescentar mais algum valor(S/N)? ')).strip().upper()[0]
    if pergunta not in 'SN':
        print('Erro digite S para SIM e N para NÃO!')
    elif pergunta in 'S':
        total += 1
listavalores.sort()
print(f'Os valores digitados foram {listavalores}')
