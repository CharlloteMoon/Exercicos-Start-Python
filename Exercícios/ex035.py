print('--- EXERCICIO 035 --- \n ANALISANDO TRIÂNGULO v1.0')
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))

if n3<n1+n2 and n2<n1+n3 and n1<n2+n3:
    print(f'Os segmentos acima PODEM formar um triângulo!')
else:
    print(f'Os segmentos acima NÃO PODEM formar um triângulo!')
