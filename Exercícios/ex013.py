print('--- EXERCICIO 013 --- \n REAJUSTE SALARIAL')
n = float(input('Quanto é o salário atual? R$'))
m = n+n*15/100
print('Um funcionário que ganhava R${:.2f}, agora vai ganhar R${:.2f}.' . format(n, m))
