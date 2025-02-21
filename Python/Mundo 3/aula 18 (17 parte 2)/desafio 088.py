# crie palpites para a mega sena, pergunte quantos jogos serão gerados e sortei 6 numeros para cada jogo entre 1 e 60 sendo que não podem se repetir. Cadastre tudo em uma lista composta
from random import randint

print('=-'* 30)
print(' '*15,'SORTEIO NÚMEROS MEGA SENA')
print('=-'* 30)
n = int(input('Quantos jogos vão ser: '))

matriz = list()
valores = list()
print('=-'*10,'Números Sorteados!','=-'*10)
for n in range(0, n):
    for v in range(0, 6):
        valores.append(randint(1, 60))
    matriz.append(valores[:])
    valores.clear()
for s in range(0, n+1):
    print(f'Jogo {s+1}: {matriz[s]}')
print('~~'* 12, 'Boa Sorte!', '~~'* 12)
