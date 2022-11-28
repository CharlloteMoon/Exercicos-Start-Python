print('--- \033[35mEXERCICIO 036\033[m --- \n \033[1;31;40mCONVERSOR DE BASES NUMÉRICAS\033[m')
n = int(input('\033[1;33mDigite um número inteiro:\033[m '))
print('''Escolha uma das bases para a conversão: 
\033[1;34m[ 1 ]\033[m converter para  \033[1;44mBINÁRIO\033[m 
\033[1;34m[ 2 ]\033[m converter para \033[1;43mOCTAL\033[m 
\033[1;34m[ 3 ]\033[m converter para \033[1;45mHEXADECIMAL\033[m''')
m = int(input('\033[1;33mQual opção:\033[m '))
if m == 1:
    x = format(n, "b")
    m = '\033[1;44mBINÁRIO\033[m'
elif m == 2:
    x = format(n, "o")
    m = '\033[1;43mOCTAL\033[m'
elif m == 3:
    x = format(n, "x")
    m = '\033[1;45mHEXADECIMAL\033[m'
print('O número \033[1;34m{}\033[m convertido para {} é igual a \033[1;31m{}\033[m' .format(n, m, x))