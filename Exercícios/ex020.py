from random import choices
print('--- EXERCICIO 020 --- \n SORTEANDO UMA ORDEM NA LISTA')
n1 = input('Primeiro aluno: ')
n2 =input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
m = choices([n1, n2, n3, n4], k=4)
print(f'A ordem de apresentação será \n {m} ')
