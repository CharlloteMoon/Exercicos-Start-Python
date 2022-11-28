from random import randint
print(f'{"Exercício 74":^40} \n{"MAIOR E MENOR VALORES EM TUPLA":^40} \n{"=" * 40}')
nums = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print(f'{"Os valores gerados são:":^40}')
for num in nums:
    print(f'{" " * 4}\033[1;35m{num:>3}\033[m', end='')
print(f'\n{"=" * 40}')
print(f'O maior valor é \033[1;36m{max(nums)}\033[m e o menor valor é \033[1;36m{min(nums)}\033[m')
