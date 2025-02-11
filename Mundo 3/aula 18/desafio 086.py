# crie um programa que crie uma matriz de dimensão 3X3 e preencha com calores lidos pelo teclado. No final mostre a matriz na tela com a formatação correta
'''
l1 = []
l2 = []
l3 = []
valores = [l1, l2, l3]
coluna = linha = 0
matriz = ''''''
            0 [  ,  , ]
            1 [  ,  , ]
            2 [  ,  , ]
               0  1  2
''''''

print('Digite os números para a matriz a seguir:')
print(matriz.center(35))

for c in range(0, 9):
    if linha == 3:
        linha = 0
        coluna += 1

    n = int(input(f'Digite um número para [{linha}][{coluna}]: '))

    valores[linha].append(n)

    linha += 1

print(f'0 {valores[0]}\n1 {valores[1]}\n2 {valores[2]}')
print('   0  1  2')
'''
# Forma do Guanabara

matriz = '''
            0 [  ,  , ]
            1 [  ,  , ]
            2 [  ,  , ]
               0  1  2
'''

print('Digite os números para a matriz a seguir:')
print(matriz.center(35))

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [Linha X Coluna] [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()