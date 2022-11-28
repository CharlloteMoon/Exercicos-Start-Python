print('--- \033[35mEXERCICIO 42\033[m --- \n  \033[1;31;40mANALISANDO TRIÂNGULOS V2.0\033[m')
n1 = float(input('\033[1;33mPrimeiro segmento:\033[m '))
n2 = float(input('\033[1;33mSegundo segmento:\033[m '))
n3 = float(input('\033[1;33mTerceiro segmento:\033[m '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    if n1 == n2 == n3:
        trian = 'EQUILÁTERO'
    elif n1 == n2 or n2 == n3 or n3 == n1:
        trian = 'ISÓSCELES'
    else:
        trian = 'ESCALENO'
    print(f'Com os segmentos \033[1;34m{n1}\033[m, \033[1;34m{n2}\033[m e \033[1;34m{n3}\033[m é possivel formar um triângulo \033[1;43m{trian}\033[m.')
else:
    print('Os segmentos acima \033[1;41mNÃO\033[m formam um triângulo.')
