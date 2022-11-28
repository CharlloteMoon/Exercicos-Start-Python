print('--- \033[35mEXERCICIO 40\033[m --- \n \033[1;31;40mCALCULO DE MÉDIA\033[m')
n1 = float(input('\033[1;34mPrimeira nota:\033[m '))
n2 = float(input('\033[1;34mSegunda nota:\033[m '))
m = (n1+n2)/2
print('Com as \033[1;34m{:.1f}\033[m e \033[1;34m{:.1f}\033[m, a sua média fica \033[1;34m{:.1f}\033[m' .format(n1, n2, m))
if m < 5:
    print('Você está \033[1;41mREPOVADO!\033[m')
elif m >= 7:
    print('Você está \033[1;42mAPROVADO!\033[m')
else:
    print('Você está de \033[1;43mRECUPERAÇÃO!\033[m')