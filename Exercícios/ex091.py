print()

from random import randint

print(f'{" Exercicio 91 ":-^30} \n{" Jogo de Dados em Python ":^30} \n')

infoJogadores = []

for jogos in range(1, 5):

    infoJogadores['jogo'] = randint(1, 6)

print(infoJogadores)

print()