print('--- EXERCICIO 64 --- \n TRATANDO VÁRIOS VALORES ')
print('~' * 25)
num = 0
count = 0
total = 0
while num != 999:
    num = int(input('Digite um número [999 para para]: '))
    count += 1
    total += num
total -= 999
count -= 1
print(f'Você digitou {count} números e a soma de todos eles é {total}.')
