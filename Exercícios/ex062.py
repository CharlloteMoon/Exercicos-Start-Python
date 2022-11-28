print('--- EXERCICO 62 --- \n SUPER PROGRESSÃO ARITMÉTRICA v3.0')
print('-=' * 15)
p1 = int(input('Primeiro termo: '))
razao = int(input('A razão: '))
pa = p1 + razao
count = 2
print(f' 1º termo {p1} ->', end=' ')
termos = 10
pergunta = 1
while not (pergunta == 0):
        while count <= termos:
                if count < termos:
                        print(f'{count}° termo {pa} ->', end='  ')
                        pa += razao
                elif count == termos:
                        print((f'{count}º termo {pa}'))
                count += 1
        pergunta = int(input('Quantos termos a mais você quer mostrar? '))
        termos += pergunta
print(f'Progessão finalizada com {count - 1} termos mostrados.')