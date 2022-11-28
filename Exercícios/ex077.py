print(f'{"Exercício 77":^40} \n{"CONTANDO VOGAIS EM TUPLA":^40} \n{"-" * 40}')
palavras = 'adeus', 'chuva', 'saudade', 'amor', 'carinho', 'python'
for p in palavras:
    print(f'A palavra \033[1;34m{p.upper()}\033[m possui as vogais:', end=' ')
    for letra in p:
        if letra in 'aeiou':
            print(f'\033[1;31m{letra}\033[m', end=' ')
    print('\n', end='')
print(f'{"-" * 40}')
