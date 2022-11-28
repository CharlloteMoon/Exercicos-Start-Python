print(f'{"Exercício 72":^35} \n{"NÚMERO POR EXTENSO":^35} \n{"=" * 35}')
numextenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'desseseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
num = 21
perg = ' '
while perg not in 'n':
    while not 0 <= num <= 20:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            print('=' * 35)
            print(f'Você digitou o número {numextenso[num].capitalize()}')
            print('=' * 35)
    perg = str(input('Quer continuar(S/N)? ')).strip().lower()[0]
    if perg in 's':
        print('=' * 35)
        num = 21
print(f'{" Fim do Programa ":=^35}')
