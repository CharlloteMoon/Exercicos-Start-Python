from random import choice
print('--- EXERCICIO 045 --- \n GAME: PEDRA, PAPEL E TESOURA ')
print('''Escolha uma opção:
[ 1 ] Pedra
[ 2 ] Tesoura 
[ 3 ] Papel''')
n = int(input('Qual opção você escolhe? '))
comp = choice(['tesoura', 'pedra', 'papel'])
print('='*15)
print(f'O computador escolheu {comp.capitalize()}')
if n == 1:
    player = 'pedra'
elif n == 2:
    player = 'tesoura'
elif n == 3:
    player = 'papel'
print(f'O jogador escolheu {player.capitalize()}')
print('='*15)
if comp == 'tesoura':
    if player == 'papel':
        campeao = 'computador ganhou!'
    elif player == 'pedra':
        campeao = 'jogador ganhou!'
    elif player == 'tesoura':
        campeao = 'empate!'
elif comp == 'pedra':
    if player == 'papel':
        campeao = 'jogador ganhou!'
    elif player == 'pedra':
        campeao = ' empate!'
    elif player == 'tesoura':
        campeao = 'compuador ganhou!'
elif comp == 'papel':
    if player == 'pedra':
        campeao = 'computador ganhou!'
    elif player == 'papel':
        campeao = 'empate!'
    elif player == 'tesoura':
        campeao = 'jogador ganhou!'
print(f'{campeao.title()}')