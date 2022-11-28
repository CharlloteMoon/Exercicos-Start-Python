print('--- EXERCICIO 67 --- \n TABUADA v3.0')
n = 0
while not n < 0:
    count = 1
    n = int(input('Quer ver a tabuada de qual valor? '))
    while count <= 10:
        if not n < 0:
            print(f'{n} x {count} = {n * count}')
            count += 1
        else:
            break
    print('=' * 25)
    count = 1
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')