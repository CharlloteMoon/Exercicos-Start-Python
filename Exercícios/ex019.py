from random import choice
print('--- EXERCICIO 019 --- \n SORTEANDO UM ITEM NA LISTA')
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
t = [n1, n2, n3, n4]
m = choice(t)
print(f'A ordem de apresentação será {m}.')
