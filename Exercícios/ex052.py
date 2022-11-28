print('--- EXERCICIO 52 --- \n NÚMEROS PRIMOS')
n = int(input('Digite um número: '))
mult = 0
for c in range(2, n):
    if (n % c == 0):
        print(f'É multiplo de {c}')
        mult += 1
if mult == 0:
    print(f'O número {n} é PRIMO!')
else:
    print(f'O número {n} NÃO é PRIMO!')
