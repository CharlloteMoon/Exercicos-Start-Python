from calendar import isleap
from datetime import date
print('--- EXERCICIO 032 --- \n ANO BISSEXTO')
n = int(input('Qual ano você quer analisar? Coloque 0 caso queira usar o ano atual: '))
if n == 0:
    n = date.today().year
m = isleap(n)
if m:
    print(f'O ano {n} é BISSEXTO.')
else:
    print(f'O ano {n} não é BISSEXTO.')