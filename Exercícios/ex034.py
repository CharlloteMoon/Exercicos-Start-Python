print('--- EXERCICIO 034 --- \n AUMENTOS MÚLTIPLOS')
n = float(input('Qual é o salário do funcionário? R$'))
if n <= 1250:
    m = n+(n*15)/100
else:
    m = n+(n*10)/100
print('Quem ganhava R${:.2f}, agora irá ganhar R${:.2f}.' .format(n, m))