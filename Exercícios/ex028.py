from random import choice
print('--- EXERCICIO 028 --- \n JOGO DE ADIVINHAÇÃO V1.0')
print('-=-' *20)
print('Tente adivinhar o número que estou pensando, vai ser de 0 a 5')
print('-=-' *20)
n = int(input('Qual número você escolhe? '))
m = choice([0, 1, 2, 3, 4, 5])
if m == n:
    print('VOCÊ GANHOU!')
else:
    print('VOCÊ PERDEU!')
print(f'O número que eu escolhi foi {m} e o número que você escolheu foi {n}.')