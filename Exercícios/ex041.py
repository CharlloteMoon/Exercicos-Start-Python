from datetime import date
print('--- \033[35mEXERCICIO 41\033[m --- \n \033[1;31;40mCLASSIFICAÇÃO DE ATLETAS\033[m')
n = int(input('\033[1;33mQual o ano do seu nascimento?\033[m '))
year = date.today().year
age = year-n
print(f'O atleta tem \033[1;34m{age} anos\033[m.')
if age <= 9:
    category = 'MIRIM'
elif age <= 14:
    category = 'INFANTIL'
elif age <= 19:
    category = 'JUNIOR'
elif age <= 25:
    category = 'SÊNIOR'
else:
    category = 'MASTER'
print(f'Sua classificação é \033[1;46m{category}\033[m')
