from time import sleep

print(f'\n{" Exercício 93 ":-^40} \n{" Cadastro de Jogador de Futebol ":^40} \n')

dadosJogador = {}

partidasGols = []

dadosJogador['nome'] = str(input('Nome do Jogador: '))

dadosJogador['partidas jogadas'] = int(input(f'Quantas partidas {dadosJogador["nome"].capitalize()} jogou? '))

print()

for c in range(0, dadosJogador['partidas jogadas']):

    partidasGols.append(int(input(f'Quantos gols {dadosJogador["nome"].capitalize()} marcou na {c + 1}ª partida? ')))

dadosJogador['gols'] = partidasGols.copy()

sleep(1)

print()

print(f'{" 1º Modo de Visualização ":-^40} \n')

sleep(0.5)

print(dadosJogador)

sleep(1.5)

print()

print(f'{" 2º Modo de Visualização ":-^40} \n')

for k, v in dadosJogador.items():
    
    sleep(0.5)
    
    print(f'{k.title()} tem o valor {v}')

sleep(1.5)
    
print()

print(f'{" 3º Modo de Visualização ":-^40} \n')

sleep(0.5)

print(f'O jogador {dadosJogador["nome"].capitalize()} fez:')

for c in range(0, dadosJogador['partidas jogadas']):
    
    sleep(0.5)
    
    print(f'{" " * 5} Na {c + 1}ª Partida fez {dadosJogador["gols"][c]} gols')

print(f'Com o total de {sum(dadosJogador["gols"])} gols! \n')