print('--- EXERCICIO 51 --- \n PROGRESSÃO ARITMÉTICA ')
print('10 Primeiros Termos')
p1 = int(input('Primeiro termo: '))
r = int(input('A razão: '))
pa = 0
for c in range(1, 11):
    pa = p1 + (c - 1) * r
    print(pa, end=' -> ')
print('FIM')