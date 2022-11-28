print('--- EXERCICIO 57 --- \n VALIDAÇÃO DE DADOS')
sexo = ' '
while not (sexo in 'MmFf'):
    sexo = str(input('Qual é o seu sexo[M/F]? ')).strip().upper()[0]
    if not (sexo in 'MmFf'):
        print('\033[1;31mErro, digite um valor válido!\033[m')
print(f'\033[1;32mO sexo {sexo.capitalize()} foi registrado com sucesso.\033[m')
