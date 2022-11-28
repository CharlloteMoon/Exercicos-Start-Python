print('--- EXERCICIO 65 --- \n MAIOR E MENOR VALOR')
p = ' '
count = media = maior =menor = add = 0
nums = []
while not (p in 'Nn'):
    while count <= add:
        n = int(input('Digite um número: '))
        count += 1
        nums.append(n)
    maior = max(nums)
    menor = min(nums)
    p = str(input('Quer conitnuar[S/N]: ')).strip().upper()
    if p == 'S':
        add += 1
    elif not (p == 'S' or p == 'N'):
        print('\033[1;41mErro, digite um valor válido!\033[m')
nums = sum(nums)
media = nums / count
print('Você digitou {} números e a média foi de {:.0f}.' .format(count, media))
print(f'O maior valor foi {maior} e o menor valor foi {menor}.')
