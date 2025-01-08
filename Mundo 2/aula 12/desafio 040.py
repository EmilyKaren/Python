# calcular a media da nota de um aluno
print('\033[36m-*-\033[m'*20)
print('Calculador de média!')
print('Tabela de classificação:\n\033[4;32mAprovado\033[m: >= 7.0\n\033[4;33mRecuperação\033[m: entre 5.0 e 6.9\n\033[4;31mReprovado\033[m: > 5.0')
n1 = float(input('Informe a primeira nota do aluno(a): '))
n2 = float(input('Informe a segunda nota do aluno(a): '))
m = (n1 + n2)/2
if m < 5.0:
    print(f'\033[4;31mREPROVADO\033[m. Sua média foi de {m:0.1f}')
elif m >= 7.0:
    print(f'\033[4;32mAPROVADO\033[m. Sua média foi de {m:0.1f}')
    if m >= 9.0:
        print('você se esforsou muito e tirou uma nota maravilhosa! Como recompensa merece uma barra de chocolate!')
else:
    print(f'\033[4;33mRECUPERAÇÃO\033[m. Sua média foi de {m:0.1f}')
print('\033[36m-*-\033[m'*20, '\n')
