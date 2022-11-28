print(f'{" DESAFIO 81 ":^30} \n{" Extraindo Dados de uma Lista ":^30} \n{"~":~^25}')

listavalores = []
pergunta = ' '
count = 0
total = 1

while pergunta not in 'N':
    while count != total:
        listavalores.append(int(input(f'Digite o {count + 1}º valor: ')))
        count += 1
    pergunta = str(input('Quer adicionar mais algum valor(S/N)? ')).strip().upper()[0]
    if pergunta not in 'SN':
        print('Digite S para SIM ou N para NÃO!')
    elif pergunta in 'S':
        total += 1
print('~' * 25)
listavalores.sort(reverse=True)
print(f'''Foram digitados {len(listavalores)} números.
Os números digitados foram {listavalores}.''')
print('O número 5', end=' ')
if 5 not in listavalores:
    print('não foi digitado e não está na lista.')
elif 5 in listavalores:
    print(f'foi digitado, e está na posição {listavalores.index(5)}.')
    