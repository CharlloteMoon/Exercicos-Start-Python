print('--- EXERCICIO 56 --- \n ANALISADOR COMPLETO')
idades = 0
idademaior = 0
nomefinal = 0
totalf = 0
for c in range(1, 5):
    print('-' * 5 + f' {c}ª PESSOA ' + '-'*5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    idades += idade
    if sexo == 'M' and idade > c:
        nomefinal = nome
        idademaior = idade
    elif sexo == 'F' and idade < 20:
        totalf += 1
print('A média de idade do grupo é de {:.0f} anos' .format(idades/4))
print('O homem mais velhor do grupo tem {} anos e se chama {}' .format(idademaior, nomefinal.capitalize()))
print(f'Ao todo são {totalf} mulheres com menos de 20 anos.')