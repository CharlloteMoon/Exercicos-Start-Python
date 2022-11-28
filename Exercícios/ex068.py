from random import randint
print('--- EXERCICIO 68 --- \n JOGO DO PAR OU ÍMPAR')
count = 0
while True:
    comp = randint(0, 10)
    print('=' * 30)
    print('Escolha um número de 0 à 10')
    jogador = int(input('Qual número você escolhe? '))
    if jogador <= 10 and jogador >= 0:
        soma = comp + jogador
        PorI = ' '
        while PorI not in 'PI':
            PorI = str(input('Você escolhe Par(P) ou Ímpar(I)? ')).strip().upper()[0]
            print('=' * 30)
            print('\033[1;41mDigite um valor válido!\033[m')
        print('=' * 60)
        print(f'A soma dos números \033[1;33m{comp}\033[m e \033[1;33m{jogador}\033[m é igual a \033[1;34m{soma}\033[m logo ele é', end=' ')
        soma %= 2
        if soma == 0:
            somaPorI = 'P'
            print('\033[1;31mPar!\033[m')
        else:
            somaPorI = 'I'
            print('\033[1;31mÍmpar!\033[m')
        if PorI == somaPorI and PorI in 'PI':
            print('\033[1;32mVocê ganhou!\033[m Vamos jogar novamente...')
            count += 1
        else:
            print('\033[1;31mVocê perdeu!\033[m')
            break
    else:
        print('\033[1;41mDigite um valor válido!\033[m')
if count >= 1:
    if count == 1:
        vz = ''
    else:
        vz = 'es'
    print('=' * 30)
    print(f'Você ganhou \033[1;33m{count}\033[m vez{vz}. \033[1;32mParabéns!\033[m')
else:
    print('=' * 75)
    print('Que pena você não ganhou nenhuma vez, mas não desanima, vamos jogar de novo!')
