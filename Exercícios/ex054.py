from datetime import date
print('--- EXERCICIO 54 --- \n GRUPO DA MAIORIDADE')
atual = date.today().year
atualmaior = int(atual) - 18
totalmaior = 0
totalmenor = 0
for c in range(1, 8):
    n = int(input(f'Qual é o {c}° ano de nascimento? '))
    if n <= atualmaior:
        totalmaior += 1
    else:
        totalmenor += 1
print(f'Ao todo tivemos {totalmaior} pessoas maiores de idade \nE também tivemos {totalmenor} pessoas menores de idade.')