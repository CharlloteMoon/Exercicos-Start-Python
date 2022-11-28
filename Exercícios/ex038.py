print('--- \033[35mEXERCICIO 38\033[m --- \n \033[1;31;40mCOMPARANDO NÚMEROS\033[m')
n1 = int(input('\033[1;33mPrimeiro número:\033[m '))
n2 = int(input('\033[1;33mSegundo número:\033[m '))
if n1 > n2:
    print('O \033[1;32mPRIMEIRO\033[m é o maior. ')
elif n1 == n2:
    print('Ambos o números são \033[1;32mIGUAIS\033[m.')
else:
    print('O \033[1;32mSEGUNDO\033[m número é maior.')