print(f'''{"Exercício 78":-^40}
{"Maior e Menor Valores na Lista":-^40}''')
valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite o {c + 1}º Valor: ')))
print(f'''{"=" * 30}
Os valores digitados são''', end=' ')
max = max(valores)
min = min(valores)
for num in valores:
    if num == max or num == min:
        print(f'\033[1;33m{num}\033[m', end=' ')
    else:
        print(f'\033[1;31m{num}\033[m', end=' ')
print(f'\nO maior número é o \033[1;33m{max}\033[m que está nas posições', end=' ')
for pos, num in enumerate(valores):
    if num == max:
        print(f'\033[1;36m{pos + 1}\033[m...', end=' ')
print(f'\nO menor número é o \033[1;33m{min}\033[m que está nas posições', end=' ')
for pos, num in enumerate(valores):
    if num == min:
        print(f'\033[1;36m{pos + 1}\033[m...', end=' ')
