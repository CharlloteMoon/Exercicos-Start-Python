print('--- \033[35mEXERCICIO 036\033[m --- \n \033[1;31;40mAPROVANDO EMPRÉSTIMO\033[m')
vc = float(input('\033[33mValor da casa: R$\033[m'))
s = float(input('\033[33mSalário do comprador: R$\033[m'))
qa = int(input('\033[33mQuantos anos de financiamento?\033[m '))
pm = vc/(qa*12)
print('Para pagar uma casa de \033[1;34mR${:.2f}\033[m em \033[1;34m{} anos\033[m a prestação será de \033[1;34mR${:.2f}\033[m.' .format(vc, qa, pm))
if pm <= (s*30/100):
    print('O Empréstimo pode ser \033[1;32mCONCEDIDO!\033[m')
else:
    print('O Empréstimo foi \033[1;31mNEGADO!\033[m')
