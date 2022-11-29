print(f'\n{" Exercício 93 ":-^40} \n{" Cadastro de Jogador de Futebol ":^40} \n')

dadosJogador = {}

partidasGols = []

dadosJogador['nome'] = str(input('Nome do Jogador: '))

dadosJogador['partidas jogadas'] = int(input(f'Quantas partidas {dadosJogador["nome"].capitalize()} jogou? '))

for c in range(0, dadosJogador['partidas jogadas']):

    partidasGols.append(int(input(f'Quantos gols {dadosJogador["nome"].capitalize()} marcou na {c + 1} partida? ')))



print()

print(dadosJogador, partidasGols)

print()