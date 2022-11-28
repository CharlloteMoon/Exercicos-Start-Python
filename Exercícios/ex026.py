print('--- EXERCICIO 026 --- \n PRIMEIRA E ÚLTIMA OCORRÊNCIA DE UMA STRING')
n = str(input('Digite uma frase: ')).lower().strip()
print(n.title())
print('A letra A aparece {} na frase. \nA primeira letra A apareceu na posição {} \nA última letra A apareceu na posição {}' .format(n.count('a'), n.find('a')+1, n.rfind('a')+1))