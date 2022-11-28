print('--- EXERCICIO 029 --- \n RADAR ELETRÔNICO')
n = int(input('Qual é a velocidade atual do carro? '))
if n > 80:
    print('MULTADO! Você excedeu o limite de velocidade que é de 80km/h \nVocê deve pagar uma multa de R${:.2f}!' .format((n-80)*7))
print('Tenha um Bom Dia! Dirija com segurança!')