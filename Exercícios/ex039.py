from datetime import date
print('--- \033[35mEXERCICIO 39\033[m --- \n \033[1;31;40mALISTAMENTO MILITAR\033[m')
n = int(input('\033[1;33mQual o ano que você nasceu?\033[m '))
atual =date.today().year
idade = atual-n
print(f'Quem nasceu em \033[1;34m{n}\033[m tem \033[1;34m{idade} anos\033[m em \033[1;34m{atual}\033[m.')
if  idade == 18:
    print('Você precisa se alistar \033[1;41mIMEDIATAMENTE!\033[m')
elif idade > 18:
    print(f'''Você já deveria ter se alistado há \033[1;31m{idade-18} anos\033[m.
Seu alistamento foi em \033[1;41m{atual-(idade-18)}!\033[m''')
else:
    print(f'''Ainda faltam \033[1;31m{18-idade} anos\033[m para o alistamento.
Seu alistamento será em \033[1;41m{atual+(18-idade)}!\033[m''')