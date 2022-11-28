print('--- \033[35mEXERCICIO 43\033[m --- \n \033[1;31;40mÍNDICE DE MASSA CORPORAL\033[m')
peso = float(input('\033[1;33mQual é o seu peso(Kg)?\033[m '))
altura = float(input('\033[1;33mQual é a sua altura(m)?\033[m '))
imc = peso/(altura**2)
print('O seu IMC  é de \033[1;34m{:.1f}\033[m' .format(imc))
if imc < 18.5:
    indice = '\033[1;43mABAIXO DO PESO!\033[m'
elif imc < 25:
    indice = 'no \033[1;42mPESO IDEAL!\033[m'
elif imc < 30:
    indice = 'com \033[1;43mSOBREPESO!\033[m'
elif imc < 40:
    indice = 'com \033[1;41mOBESIDADE!\033[m'
else:
    indice = 'com \033[1;41mOBESIDADE MÓRBIDA!\033[m'
print(f'Você está {indice}')
