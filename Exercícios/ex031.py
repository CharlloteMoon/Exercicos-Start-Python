print('--- EXERCICIO 031 --- \n CUSTO DA VIAGEM')
n = int(input('Qual é a distância da sua viagem? '))
print(f'Para uma viagem de {n}km ')
if n <= 200:
    m = n*0.50
else:
    m = n*0.45
print('O valor a se pagar pela viagem é R${:.2f}' .format(m))