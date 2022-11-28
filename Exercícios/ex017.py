from math import hypot
print('--- EXERCICIO 017 ---')
n1 = float(input('Comprimento do cateto oposto: '))
n2 = float(input('Comprimento do cateto adjacente: '))
m = hypot(n1, n2)
print('A hipotenusa vai medir {:.2f}' .format(m))