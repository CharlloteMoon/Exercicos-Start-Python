print('--- EXERCICIO 011 --- \n TINTA PARA PAREDE')
n1 = float(input('Qual é a altura da parede em metros? '))
n2 = float(input('Qual é a largura da parede em metros? '))
a = n1*n2
t = a/2
print('Sua parede tem dimensão de {}m X {}m e sua área total da parede é {:.2f}m².' .format(n1, n2, a))
print('Para pintar essa parede, você irá precisar de {:.1f}l de tinta. \n (1l para 2m²)' . format(t))
