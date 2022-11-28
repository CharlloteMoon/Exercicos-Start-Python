print('--- EXERCICIO 69 --- \n ANÁLISE DE DADOS DO GRUPO')
count = 1
countm = count18 = countf20 = 0
erro = '\033[1;41mErro, digite um valor válido!\033[m'
while True:
    pergunta = sexo = ' '
    print('=' * 30)
    idade = int(input(f'Digite a idade da {count}ª pessoa: '))
    while sexo not in 'MF':
        sexo = str(input(f'Digite o sexo(M/F) da {count}ª pessoa: ')).strip().upper()[0]
        if sexo not in 'MF':
            print(erro)
    if idade >= 18:
        count18 += 1
    if sexo == 'M':
        countm += 1
    if sexo == 'F' and idade < 20:
        countf20 += 1
    print('=' * 30)
    while pergunta not in 'NS':
        pergunta = str(input('Quer acrescentar mais alguma pessos(S/N)? ')).strip().upper()[0]
        if pergunta not in 'NS':
            print(erro)
        elif pergunta in 'S':
            count += 1
    if pergunta in 'N':
        print('=' * 30)
        break
if count == 1:
    pluralcount = ''
else:
    pluralcount = 's'
if count18 == 1:
    plural18 = ''
else:
    plural18 = 's'
if countm == 1:
    pluralm = 'm'
else:
    pluralm = 'ns'
if countf20 == 1:
    pluralf = ''
else:
    pluralf = 'es'
print(f'''No grupo de {count} pessoa{pluralcount}: 
a) Possui {count18} pessoa{plural18} com 18 anos ou mais. 
b) Possui {countm} home{pluralm} no grupo.
c) Possui {countf20} mulher{pluralf} com menos de 20 anos no grupo.''')
 