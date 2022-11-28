print('--- EXERCICIO 033 --- \n MAIOR E MENOR VALORES')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
menor = n1
maior = n1
if n2 < n1:
    menor = n2
if n3 < n1:
    menor = n3
print(f'O menor número digitado é {menor}.')
if n2 > n1:
    maior = n2
if n3 > n1:
    maior = n3
print(f'O maior número digitado é {maior}.')