print('--- EXERCICIO 55 --- \n MAIOR E MENOR DA SEQUÊNCIA')
maiorpeso = 0
menorpeso = 0
pesos = []
for c in range(1, 6):
    peso = float(input(f'Qual é o peso da {c}ª pessoa? '))
    pesos.append(peso)
maiorpeso = max(pesos)
menorpeso = min(pesos)
print('O maior peso lido foi de {:.1f}Kg \nO menor peso lido foi de {:.1f}Kg' .format(maiorpeso, menorpeso))