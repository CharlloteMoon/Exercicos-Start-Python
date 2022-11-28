from time import sleep

print(f'\033[1;36m{" Exercício 89 ":-^30}\033[m \n{" Boletim com Listas Compostas ":^30}')

print()

aluno = []
alunos = []

countAlunos = 0
totalAlunos = 1

while True:
    while countAlunos != totalAlunos:
        print(f'\033[1;41m{f" {totalAlunos}º Aluno(a) ":^30}\033[m')
        nome = str(input(f'\033[1;30;47m{" Nome: ":<5}\033[m '))

        aluno.append(nome)

        for c in range(1, 3):
            nota = float(input(f'\033[1;30;47m{f" {c}ª Nota: ":<8}\033[m '))
            aluno.append(nota)

        alunos.append(aluno[:])

        aluno.clear()

        countAlunos += 1

    print(f'\033[1;47m{" " * 30}\033[m')

    questSOrN = str(input(f'\033[1;30;41m{" Adicionar mais aluno(S/N)? "}\033[m ')).upper().strip()[0]

    if questSOrN in 'S':

        totalAlunos += 1

        print(f'\033[1;47m{" " * 30}\033[m')

    elif questSOrN in 'N':

        break

    else:

        print(f'\033[1;47m{" " * 30}\033[m')

        print(f'\033[1;31;40m{" Erro! Coloque um valor válido! ":^30}\033[m')

print(f'\033[1;47m{" " * 30}\033[m')



print(f'\033[1;41m{" BOLETIM ":^30}\033[m \n\033[1;41m{" N0.  ":<3} {"NOME":<5} {"NOTA ":>17}\033[m ')

sleep(1)

for c in range(0, len(alunos)):

    print(f'\033[1;41m{f"{c + 1}.":^5} {f" {alunos[c][0].title()}":<16} {f" {(alunos[c][1] + alunos[c][2]) / 2}":^6} \033[m')

    sleep(1)

print(f'\033[1;41m{" " * 30}\033[m')

sleep(1)

while True:

    verNotas = int(input('\033[1;30;41mQuer ver qual nota(999 para sair)? \033[m '))

    if verNotas == 999:
        break

    elif verNotas <= len(alunos):

        sleep(0.5)

        print(f'\033[1;41m{" " * 30}\033[m \n\033[1;41m {f"{alunos[verNotas - 1][0].capitalize()}":<15} {f"{alunos[verNotas - 1][1]}   {alunos[verNotas - 1][2]}":^13}\033[m \n\033[1;41m{" " * 30}\033[m')

        sleep(1)

    else:

        print(f'\033[1;37;41m{" " * 30}\033[m \n\033[1;31;40m{" Erro! Digite um valor válido! ":^29}\033[m \n\033[1;37;41m{" " * 30}\033[m')
