print('--- EXERCICIO 70 --- \n ESTATÍSTICAS EM PRODUTOS')
count = 1
soma = count1000 = precomin = 0
precos = []
nomemin = ' '
while True:
    pergunta = ' '
    print('=' * 30)
    nomeprod = str(input(f'Qual é o nome do {count}º produto? ')).strip()
    precoprod = float(input(f'Qual é o preço do {count}º produto? R$'))
    precos.append(precoprod)
    menorpreco = min(precos)
    if precoprod == menorpreco:
        nomemin = nomeprod
    if precoprod >= 1000:
        count1000 += 1
    soma += precoprod
    while pergunta not in 'NS':
        print('=' * 30)
        pergunta = str(input('Quer acrescentar mais um produto(S/N)? ')).strip().upper()[0]
        if pergunta in 'S':
            count += 1
        if pergunta not in 'SN':
            print('\033[1;41mErro, digite um valor válido!\033[m')
    if pergunta in 'N':
        print('=' * 30)
        break
if count == 1:
    pluralCount = ''
else:
    pluralCount = 's'
if count1000 == 1:
    pluralMilProd = ''
    pluralMilCus = ''
else:
    pluralMilProd = 's'
    pluralMilCus = 'm'
print(f'''Você digitou {count} produto{pluralCount} 
a) O total da compra é de R${soma:.2f}.
b) Na compra temos {count1000} produto{pluralMilProd} que custa{pluralMilCus} mais de R$1000.
c) O produto mais barato da sua compra é {nomemin.capitalize()} que custa R${menorpreco:.2f}''')
