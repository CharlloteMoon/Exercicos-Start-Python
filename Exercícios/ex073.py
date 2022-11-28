print(f'{"Exercício 73":^40} \n{"TUPLAS COM TIMES DE FUTEBOL":^40} \n{"=" * 40}')
times = 'palmeiras', 'flamengo', 'fluminense', 'corinthians', 'internacional', 'athletico-PR', 'atlético-MG', 'santos', 'américa-MG', 'goiás', 'bragantino', 'fortaleza', 'são paulo', 'botafogo', 'ceará', 'coritiba', 'cuiabá', 'avaí', 'atlético-GO', 'juventude'
print('Os times do Brasileirão são', end=' ')
for c in range(0, len(times)):
    if c <= 18:
        print(f'\033[1;33m{times[c].title()}\033[m,', end=' ')
    elif c == 19:
        print(f'\033[1;33m{times[c].title()}\033[m')
print('=' * 40)
print('Os 5 primeiros colocados são', end=' ')
for c in range(0, 5):
    if c <= 3:
        print(f'\033[1;33m{times[c].title()}\033[m,', end=' ')
    elif c == 4:
        print(f'\033[1;33m{times[c].title()}\033[m')
print("=" * 40)
print('Os 4 últimos times são', end=' ')
for c in range(16, len(times)):
    if c <= 18:
        print(f'\033[1;33m{times[c].title()}\033[m, ', end=' ')
    elif c == 19:
        print(f'\033[1;33m{times[c].title()}\033[m')
print('=' * 40)
print('Os times em ordem alfabética é', end=' ')
timesorg = sorted(times)
for c in range(0, len(timesorg)):
    if c <= 18:
        print(f'\033[1;33m{timesorg[c].title()}\033[m, ', end=' ')
    elif c == 19:
        print(f'\033[1;33m{timesorg[c].title()}\033[m')
print('=' * 40)
print(f'O time do \033[1;33mSantos\033[m está na \033[1;36m{times.index("santos") + 1}\033[mª posição')
