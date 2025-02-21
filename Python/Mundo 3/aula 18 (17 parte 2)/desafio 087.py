# faça o mesmo que o desafio anterior, porem mostre: 
#   a soma de todos os valores pares
#   a soma dos valores da terceira coluna
#   o maior valor da segunda linha
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
print('=-' * 30)
pares = 0
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
print(f'A soma dos valores pares foi {pares}')

coluna3 = 0
for l in range(0, 3):
    coluna3 += matriz[l][2]
print(f'A soma dos valores da 3º coluna foi {coluna3}')

for l in range(0, 3):
    if matriz[l][2] > 0 or matriz[l][2] > maior:
        maior = matriz[l][2]
print(f'O maior valor da segunda linha foi {maior}')
