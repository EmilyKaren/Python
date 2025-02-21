'''
Todo codigo de cor no estilo ANSI vai começar com:
    \033[style;text;backm
    \033[0;33;44m
    \033[m -> configuracao padrao do terminal

Codigo introduorio/basico
style           text         back
 0 - nada       97 - white   107 - branco
 1 - negrito    30 - black   40 - preto
 4 - sublinhado 31 - red     41 - vermelho
 7 - negativo   32 - green   42 - verde
                33 - yellow  43 - amarelo
                34 - blue    44 - azul
                35 - magenta 45 - magenta
                36 - cyan    46 - ciano
                37 - grey    47 - cinza

'''
# pratica
print('\033[1;32;107mOlá, Mundo!\033[m\n')
print('\033[41mTeste de Cores.\033[m\n')
print('\033[4;32mÉ divertido brincar com as cores\033[m\n')
print('\033[7;33;44mInversão de cores\033[m\n')
a = 9
b = 4
print(f'Os valores são \033[4;31m{a}\033[m e \033[4;34m{b}\033[m\n')
print('\033[4;97;45mCada Fase\033[m De \033[1;36;47mUma Cor\033[m\n')

'''nome = 'Guanabara'
cores = {
    'limpar','\033[m',
    'azul','\033[34m',
    'amarelo','\033[33m',
    'pretobranco','\033[7;97m',}
print(f'Outra forma de formatar {azul}cores{limpar} ensinado pelo {amarelo}{nome}{limpar}!!!') não consegui fazer'''