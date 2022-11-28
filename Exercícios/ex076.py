print(f'{"Exercício 76":^40} \n{"LISTA DE PREÇOS COM TUPLA":^40} \n{"-" * 40}')
prods = 'arroz', 15.50, 'feijao', 10.60, 'cenoura', 4
count = 0
while count != len(prods):
    print(f'{prods[count].capitalize():.<30}R$', end='')
    count += 1
    print(f'{prods[count]:>8.2f}')
    count += 1
print('-' * 40)
