print(f'{" DESAFIO 83 ":^30} \n{" Validando Expressões Matemáticas ":^30} \n{"~" * 25}')

expressao = str(input('Digite a expressão: '))
parentes1 = parentes2 = 0

for parentes in expressao:
    if parentes == '(':
        parentes1 += 1
    elif parentes == ')':
        parentes2 += 1

print(f'A expressão {expressao}', end=' ')
if parentes1 == parentes2:
    print('está correta!')
else:
    print('está incorreta!')
