print('--- EXERCICIO 022 --- \n ANALISADOR DE TEXTOS')
n = str(input('Digite seu nome completo: ')).strip()
nu = n.upper()
nl = n.lower()
s = n.split()
ql = len(n)-n.count(' ')
fn = s[0]
fnca = len(fn)
print(f'Analisando o seu nome... \nSeu nome em maiúsculas é {nu} \nSeu nome em minúsculas é {nl} \nSeu nome tem ao todo {ql} letras \nSeu primeiro nome é {fn.capitalize()} e ele tem {fnca} letras ')