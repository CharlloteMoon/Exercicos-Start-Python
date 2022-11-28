print('--- EXERCICIO 60 --- \n CÁLCULO DO FATORIAL')
n = int(input('Digite um número para calcular o seu fatorial: '))
multi = n
print(f'Calculando {n}! =', end=' ')
while not (n == 1):
    print(f'{n} x', end=' ')
    n -= 1
    multi *= n
print(f'1 = {multi}')
