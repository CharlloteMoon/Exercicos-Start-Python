print('{: ^50} \n {: ^50}' .format('EXERICIO 71', 'SIMULADOR DE CAIXA ELETRÔNICO'))
count50 = count20 = count10 = count1 = 0
rest50 = rest20 = rest10 = rest1 = 0
print('=' * 50)
print('\033[1;33mNeste caixa apenas cédulas de \033[1;34mR$50 R$20 R$10 R$1\033[m.')
print('=' * 50)
valor = int(input('Qual é o valor que você gostaria de sacar? R$'))
print('=' * 50)
while valor != 0:
    rest50 = valor % 50
    rest20 = valor % 20
    rest10 = valor % 10
    rest1 = valor % 1
    if rest50 == 0:
        valor -= 50
        count50 += 1
    else:
        if rest20 == 0:
            valor -= 20
            count20 += 1
        else:
            if rest10 == 0:
                valor -= 10
                count10 += 1
            else:
                if rest1 == 0:
                    valor -= 1
                    count1 += 1
print('Iremos te entregar...')
if count50 >= 1:
    if count50 == 1:
        plural50 = ''
    else:
        plural50 = 's'
    print(f' *{count50} cédula{plural50} de R$50*')
if count20 >= 1:
    if count20 == 1:
        plural20 = ''
    else:
        plural20 = 's'
    print(f' *{count20} cédula{plural20} de R$20*')
if count10 >= 1:
    if count10 == 1:
        plural10 = ''
    else:
        plural10 = 's'
    print(f' *{count10} cédula{plural10} de R$10*')
if count1 >= 1:
    if count1 == 1:
        plural1 = ''
    else:
        plural1 = 's'
    print(f' *{count1} cédula{plural1} de R$1*')
