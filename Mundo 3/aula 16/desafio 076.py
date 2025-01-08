# crie uma tupla com nomes de produtos e seus preços e no final mostre uma lista com o nome do produto e seu preço. ex
'''
lapis...............R$ 1.50
borracha............R$ 0.50
'''
# forma do guanabara:
print('-=' *21)
print(f'{'LISTAGEM DE PREÇOS':^40}') # o :^ Centraliza
print('-=' *21)
listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='') # o :< significa alinhado a esquerda e preencher com . em 30 espaços
    else:
        print(f'R${listagem[pos]:>7.2f}') # :> alinha a direita

'''
# jeito que eu fiz - tive dificuldade nesse
titulo = 'Lista de Preços'

tupla = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('=' *50)
print(titulo.center(50))
print('-' * 50)

for pos, item in enumerate(tupla):
    if pos == 0 or pos == 1:
        print(item, end='')
        if pos == 0:
            print('.'*25,'R$', end=' ')
        elif pos == 1:
            print(' ')
    if pos == 2 or pos == 3:
        print(item, end='')
        if pos == 2:
            print('.'*22,'R$', end=' ')
        elif pos == 3:
            print(' ')
    if pos == 4 or pos == 5:
        print(item, end='')
        if pos == 4:
            print('.'*23,'R$', end=' ')
        elif pos == 5:
            print(' ')
    if pos == 6 or pos == 7:
        print(item, end='')
        if pos == 6:
            print('.'*24,'R$', end=' ')
        elif pos == 7:
            print(' ')
    if pos == 8 or pos == 9:
        print(item, end='')
        if pos == 8:
            print('.'*18,'R$', end=' ')
        elif pos == 9:
            print(' ')
    if pos == 10 or pos == 11:
        print(item, end='')
        if pos == 10:
            print('.'*22,'R$', end=' ')
        elif pos == 11:
            print(' ')
    if pos == 12 or pos == 13:
        print(item, end='')
        if pos == 12:
            print('.'*23,'R$', end=' ')
        elif pos == 13:
            print(' ')
    if pos == 14 or pos == 15:
        print(item, end='')
        if pos == 14:
            print('.'*23,'R$', end=' ')
        elif pos == 15:
            print(' ')
    if pos == 16 or pos == 17:
        print(item, end='')
        if pos == 16:
            print('.'*25,'R$', end=' ')
        elif pos == 17:
            print(' ')
'''
