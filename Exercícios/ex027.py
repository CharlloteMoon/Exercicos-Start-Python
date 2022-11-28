print('--- EXERCICIO 027 --- \n PRIMEIRO E ÚLTIMO NOME DE UMA PESSOA')
n = str(input('Digite seu nome completo: ')).strip()
s = n.split()
print(f'Muito prazer em te conhecer! \nSeu primeiro nome é {s[0].capitalize()} \nSeu último nome é {s[len(s)-1].capitalize()}')
