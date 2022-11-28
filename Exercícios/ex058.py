from random import randint
print('--- EXERCICIO 58 --- \n JOGO DA ADIVINHAÇÃO v2.0')
print('Prazer sou o seu computador... \nBora jogar um jogo? Vou pensar em um número de 0 à 10. \nSerá que consegue adivinhar qual número estou pensando?')
computador = randint(0, 10)
jogador = 11
count = 0
while jogador != computador:
    jogador = int(input('Qual número estou pensando? '))
    count += 1
    if jogador < computador:
        print('Mais... Tente outra vez...')
    elif jogador > computador:
        print('Menos... Tente outra vez...')
if count == 1:
    escrita = 'tentativa'
else:
    escrita = 'tentativas'
print(f'Acertou! Foram {count} {escrita}.')