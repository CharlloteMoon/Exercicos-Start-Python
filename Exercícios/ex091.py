print()

from random import randint
from time import sleep

print(f'{" Exercicio 91 ":-^40} \n{" Jogo de Dados em Python ":^40} \n')

infoJogadores = {}

for jogos in range(1, 5):

    infoJogadores[f'Jogador {jogos}'] = randint(1, 6)

for k, v in infoJogadores.items():

    sleep(0.5)

    print(f'{f" O {k}  tirou o número {v} ":^40}')

sleep(1)

print(f'\n{" RANKING ":-^40} \n')

count = 1

for i in sorted(infoJogadores, key = infoJogadores.get, reverse=True):
    
    sleep(0.5)

    print(f'{f" {count}º Lugar - {i.capitalize()} com o {infoJogadores[i]} ":^40}')

    count += 1

print()