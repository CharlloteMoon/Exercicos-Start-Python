print('--- EXERCICIO 66 --- \n VÁRIOS NÚMEROS COM FLAG')
print('=' * 25)
soma = 0
count = 1
while True:
    n = int(input(f'Digite o {count}º valor [999 para parar]: '))
    if n != 999:
        count += 1
    else:
        break
    soma += n
count -= 1
print( f'A soma dos {count} valores é igual a {soma}.')
print('=' * 25)
