print(f'\033[1;35m{" Exercício 90 ":-^30}\033[m \n{" Dicionário em Python ":^30} \n')

dados = {'nome': str(input('Nome do aluno(a): ')), 'média': float(input('Média do aluno(a): '))}

print()

print(f'O(a) aluno(a) {dados["nome"].capitalize()} com a média {dados["média"]} está:')

if dados['média'] > 7:

    print(f'\033[1;30;42m{" APROVADO ":^30}\033[m')

elif 5 <= dados['média']:

    print(f'\033[1;30;43m{" RECUPERAÇÃO ":^30}\033[m')

else:

    print(f'\033[1;30;41m{" REPROVADO ":^30}\033[m')