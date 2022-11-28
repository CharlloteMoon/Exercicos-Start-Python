print('--- \033[35mEXERCICIO 44\033[m --- \n \033[1;31;40m GERENCIADOR DE PAGAMENTOS \033[m')
print('-=-'*5, '\033[1;43m LOJAS JOINHA \033[m', '-=-'*5)
preço = float(input('\033[1;33mDigite o preço do produto: R$\033[m'))
print('''\033[1;33mEscolha a forma de pagamento:\033[m
\033[1;41m [ 1 ]  \033[1;30;44m à vista dinheiro/cheque \033[m
\033[1;41m [ 2 ]  \033[1;30;44m à vista cartão \033[m
\033[1;41m [ 3 ]  \033[1;30;44m 2x no cartão \033[m
\033[1;41m [ 4 ]  \033[1;30;44m 3x ou mais no cartão \033[m''')
formapagamento = int(input('\033[1;33mQual é a opção?\033[m '))
if formapagamento == 1:
    preçofinal = preço - (preço * 10 / 100)
    print('O produto que custa R${:.2f}, terá 10% de desconto, custando agora R${:.2f}.' .format(preço, preçofinal))
elif formapagamento == 2:
    preçofinal = preço - (preço*5/100)
    print('O produto que custa R${:.2f}, terá desconto de 5%, ficando R${:.2f}.' .format(preço, preçofinal))
elif formapagamento == 3:
    preçofinal = preço/2
    print('O produto que custa R${:.2f} não tera desconto em 2x no cartão, ficando 2 parcelas de R${:.2f}.' .format(preço, preçofinal))
elif formapagamento == 4:
    parcelas = int(input('\033[1;33mQuantas parcelas?\033[m '))
    preçofinal = preço + (preço * 20 / 100)
    valormes = preço / parcelas
    print('O produto que custa R${:.2f}, em {} parcelas de R${:.2f} com juros, vai custar R${:.2f}.' .format(preço, parcelas,valormes, preçofinal))
