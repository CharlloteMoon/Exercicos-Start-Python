from random import randint
from time import sleep

print(f'\033[1;36m{" Exercício 88 ":-^30}\033[m \n{" Palpites para a MEGA SENA ":^30}\n')

jogoMegaSena = []
jogosDaMega = []

count = 0

jogosPergunta = int(input('Quantos jogos você quer? '))


while count != jogosPergunta:

    jogoMegaSena.clear()

    for c in range(1, 7):
        jogoMegaSena.append(randint(1, 60))

    jogosDaMega.append(jogoMegaSena[:])

    count += 1

if jogosPergunta <= 1:
    plural = ''
else:
    plural = 's'

print(f'\n \033[1;30;42m{f" Sorteando seu{plural} jogo{plural} ":^25}\033[m')

sleep(1)

print()

for c in range(0, len(jogosDaMega)):

    print(f'Jogo Mega Sena\033[1;32m{f"#{c + 1}":>3}\033[m: \033[1;30;42m {sorted(jogosDaMega[c])} \033[m')

    sleep(1)