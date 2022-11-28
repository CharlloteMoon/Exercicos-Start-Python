from time import sleep
print('--- EXERCICIO 59 --- \n MENU DE OPÇÕES')
resposta = 0
count = 1
numeros = []
print('-=' * 15)
while resposta != 5:
    while not (count == 3):
        n = int(input(f'Digite o {count}º valor: '))
        count += 1
        numeros.append(n)
    sleep(0.4)
    print('-=' * 15)
    print('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior número \n[ 4 ] novos números \n[ 5 ] sair do programa')
    num1 = numeros[0]
    num2 = numeros[1]
    resposta = int(input('Qual é a sua opção? '))
    if resposta == 1:
        print(f'\033[1;32mA soma dos números {num1} e {num2} é igual a {num1 + num2}.\033[m')
    elif resposta == 2:
        print(f'\033[1;32mA multiplicação dos números {num1} e {num2} é igual a {num1 * num2}.\033[m')
    elif resposta == 3:
        print(f'\033[1;32mEntre os números {num1} e {num2} o maior resultado é o {max(numeros)}.\033[m')
    elif resposta == 4:
        count = 1
        numeros.clear()
        print('-=' * 15 + '\nInforme os novos números...')
    elif resposta == 5:
        print('\033[1;33mSaindo do programa...\033[m')
    else:
        print('\033[1;41mErro, tente novamente com uma respota valida!\033[m')
    sleep(1.5)
print('-=' * 15)
print('\033[1;31mPrograma Finalizado\033[m')
