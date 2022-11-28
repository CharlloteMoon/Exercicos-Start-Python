print('--- EXERCICIO 61 --- \n PROGRESSÃO ARIYMÉTICA v2.0')
print('-=' * 15)
p1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
count = 1
pa = p1 + razao
print(f'{p1} ->', end=' ')
while not(count == 10):
    print(f'{pa} ->', end=' ')
    pa += razao
    count += 1
print('Fim ')