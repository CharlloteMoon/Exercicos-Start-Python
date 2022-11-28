print('--- EXERCICIO 023 ---\n SEPARANDO DÍGITOS DE UM NÚMERO')
n = int(input('Informe um número: '))
u = n//1%10
d = n//10%10
c = n//100%10
m = n//1000%10
print('Analisando o número {} \nUnidade: {} \nDezena: {}  \nCentena: {} \nMilhar: {} ' .format(n, u, d, c, m))
