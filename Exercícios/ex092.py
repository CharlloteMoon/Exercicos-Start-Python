from datetime import date

print(f'\n{" Exercício 92 ":-^40} \n{" Cadastro de Trabalhadores em Python ":^40} \n')

dados = {}

dados['nome'] = str(input('Qual o seu nome? '))

dados['ano de nascimento'] = int(input('Qual seu ano de nascimento? '))

dados['idade'] = date.today().year - dados['ano de nascimento']

dados['CTPS'] = int(input('Qual o número da sua CTPS(0 para nenhum)? '))

if dados['CTPS'] != 0:

    dados['ano de contratação'] = int(input('Qual ano você foi contratado? '))

    dados['salário'] = float(input('Qual o valor do salário? '))

    dados['aposentatoria'] = dados['idade'] + (35 - (date.today().year - dados['ano de contratação']))

print(f'\n \n{" Dados Cadastrais ":-^40}\n')

count = 1

for k, v in dados.items():

    print(f'{f" {k.title()}: {v} "}', end='')

    if count == 3 or count == 7:

        print('anos', end='')

    print('\n', end='')

    count += 1

print()