print('--- EXERCICIO 50 --- \n SOMA DE PARES')
soma = 0
numeros = []
for c in range(1, 7):
    print(f'--- {c}° Número ---')
    n = int(input('Digite o número: '))
    numeros.append(n)
    if n % 2 == 0:
        soma += n
print(f'Os números {numeros}')
print(f'A soma dos números pares é igual a {soma}.')