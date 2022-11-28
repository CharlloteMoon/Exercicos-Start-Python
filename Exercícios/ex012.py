print('--- EXERCICIO 012 --- \n APLICADOR DE DESCONTO')
n = float(input('Qual o preço do produto? R$'))
d = n-n*5/100
print('O produto que custava R${:.2f}, na promoção de 5% vai custar R${:.2f}.' .format(n, d))
