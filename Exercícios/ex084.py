print(f'''\033[1;36m{" Exercício 84 ":-^30}\033[m 
{"Lista Composta e Análise de Dados":^30}''')

nome = []
peso = []
pesos = []
pessoasEPesos = []
totalPessoas = 1
countPessoas = maiorPeso = menorPeso = 0
perguntaSOrN = ' '
pessoasComMaiorPeso = []
pessoasComMenorPeso = []

while True:

    while countPessoas != totalPessoas:

        peso.clear()
        nome.clear()

        print(f'\n{f" {totalPessoas}ª Pessoa ":-^30}')
        nome.append(str(input('Nome: ')))
        peso.append(float(input('Peso (Kg): ')))

        nome.append(peso[:])
        pesos.append(peso[:])
        pessoasEPesos.append(nome[:])

        countPessoas += 1

    perguntaSOrN = str(input('\nQuer adicionar mais dados de pessoas(S/N)? ')).strip().upper()[0]

    if perguntaSOrN in 'S':
        totalPessoas += 1

    if perguntaSOrN in 'N':
        break

    if perguntaSOrN not in 'SN':
        print('\033[1;41m Erro, apenas S para SIM ou N para NÃO \033[m')

menorPeso = min(pesos)
maiorPeso = max(pesos)

for c in range(0, totalPessoas):

    if pessoasEPesos[c][1] == maiorPeso:
        pessoasComMaiorPeso.append(pessoasEPesos[c][0])

    if pessoasEPesos[c][1] == menorPeso:
        pessoasComMenorPeso.append(pessoasEPesos[c][0])

if totalPessoas <= 1:
    pluralQuantidadePessoas = '.'
else:
    pluralQuantidadePessoas = 's.'

print(f'''\n{"-" * 30}
Foram adicionados {totalPessoas} pessoa{pluralQuantidadePessoas}
O peso mais pesado registrado foi o de {maiorPeso[0]:.2f}Kg, sendo o de {pessoasComMaiorPeso}.
O peso mais leve registrado foi o de {menorPeso[0]:.2f}Kg, sendo o de {pessoasComMenorPeso}.''')
