# sortei números de 1 a 6 e mostre a colocação de cada jogador na ordem decrescente
'''
import random

jogadores = dict()
colocação = dict()
for i in range(0, 4):
    i += 1
    jogadores[f'j{i}'] = random.randint(1, 6)

    if i == 1:
        colocação = jogadores[f'j{i}']
    elif jogadores[f'j{i}'] < jogadores[f'j{i - 1}']:
        colocação[i-1] = jogadores[f'j{i - 1}']

print(jogadores)
print(colocação)
'''

from random import randint
from time import sleep
from operator import itemgetter

jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}
ranking = list()
print('== VALORES SORTEADOS ==')

for k, v, in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
# Sorted coloca em ordem crescente, key serve para falar qual valor deve ser ordenado no caso as informações na posição 1, reverse faz com que ordene em ordem decrescente
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('== RANKING DOS JOGADORES ==')
for i, v, in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
